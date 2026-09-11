import os
import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

import firebase_admin
from firebase_admin import credentials, db


# =========================================================
# RIPON-MANGO LICENSE SERVER
# =========================================================

APP_ID = "RIPON-MANGO"

DB_URL = (
    "https://ripon-mango-default-rtdb."
    "asia-southeast1.firebasedatabase.app"
)

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", "8080"))


# =========================================================
# FIREBASE INIT
# =========================================================

service_account_json = os.environ.get(
    "FIREBASE_SERVICE_ACCOUNT_JSON"
)

if not service_account_json:
    raise RuntimeError(
        "FIREBASE_SERVICE_ACCOUNT_JSON is not configured."
    )

try:
    service_account_info = json.loads(service_account_json)
except json.JSONDecodeError:
    raise RuntimeError(
        "FIREBASE_SERVICE_ACCOUNT_JSON contains invalid JSON."
    )

if not firebase_admin._apps:
    cred = credentials.Certificate(service_account_info)

    firebase_admin.initialize_app(
        cred,
        {
            "databaseURL": DB_URL
        }
    )


# =========================================================
# HELPERS
# =========================================================

def send_json(handler, status, data):

    body = json.dumps(
        data,
        ensure_ascii=False
    ).encode("utf-8")

    handler.send_response(status)

    handler.send_header(
        "Content-Type",
        "application/json; charset=utf-8"
    )

    handler.send_header(
        "Content-Length",
        str(len(body))
    )

    handler.send_header(
        "Cache-Control",
        "no-store"
    )

    handler.end_headers()

    handler.wfile.write(body)


def valid_key_format(key):

    if not isinstance(key, str):
        return False

    key = key.strip().upper()

    return (
        key.startswith("MANGO-")
        and len(key) == 20
    )


def check_expiry(expiry):

    if not expiry:
        return True

    if str(expiry).strip().lower() == "lifetime":
        return True

    expiry = str(expiry).strip()

    formats = [
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d"
    ]

    for fmt in formats:

        try:

            expiry_dt = datetime.strptime(
                expiry,
                fmt
            )

            return datetime.now() < expiry_dt

        except ValueError:
            continue

    return False


# =========================================================
# LICENSE CHECK
# =========================================================

def check_license(payload):

    key = str(
        payload.get("key", "")
    ).strip().upper()

    app_id = str(
        payload.get("app_id", "")
    ).strip()

    hwid = str(
        payload.get("hwid", "")
    ).strip()

    device_model = str(
        payload.get("device_model", "")
    ).strip()

    android_version = str(
        payload.get("android_version", "")
    ).strip()

    app_version = str(
        payload.get("app_version", "")
    ).strip()


    # -----------------------------------------------------
    # APP CHECK
    # -----------------------------------------------------

    if app_id != APP_ID:

        return {
            "ok": False,
            "message": "Invalid application."
        }


    # -----------------------------------------------------
    # KEY FORMAT
    # -----------------------------------------------------

    if not valid_key_format(key):

        return {
            "ok": False,
            "message": "Invalid key format."
        }


    # -----------------------------------------------------
    # HWID
    # -----------------------------------------------------

    if not hwid or len(hwid) < 5:

        return {
            "ok": False,
            "message": "Invalid device ID."
        }


    # -----------------------------------------------------
    # FIREBASE
    # -----------------------------------------------------

    ref = db.reference(
        f"keys/{key}"
    )

    data = ref.get()


    if not isinstance(data, dict):

        return {
            "ok": False,
            "message": "Key not found."
        }


    # -----------------------------------------------------
    # APP ID
    # -----------------------------------------------------

    stored_app = data.get("app_id")

    if stored_app and stored_app != APP_ID:

        return {
            "ok": False,
            "message": "Key belongs to another application."
        }


    # -----------------------------------------------------
    # APPROVED
    # -----------------------------------------------------

    if data.get("approved") is not True:

        return {
            "ok": False,
            "message": "Key is not approved."
        }


    # -----------------------------------------------------
    # ACTIVE
    # -----------------------------------------------------

    if data.get("active") is not True:

        return {
            "ok": False,
            "message": "Key is disabled."
        }


    # -----------------------------------------------------
    # EXPIRY
    # -----------------------------------------------------

    expiry = data.get(
        "expiry",
        "Lifetime"
    )

    if not check_expiry(expiry):

        return {
            "ok": False,
            "message": "Key has expired."
        }


    # -----------------------------------------------------
    # HWID BIND
    # -----------------------------------------------------

    saved_hwid = str(
        data.get("hwid", "")
    ).strip()


    # First device
    if not saved_hwid:

        ref.update({
            "hwid": hwid,
            "device_model": device_model,
            "android_version": android_version,
            "last_app_version": app_version
        })


    # Different device
    elif saved_hwid != hwid:

        return {
            "ok": False,
            "message": (
                "This key is already linked "
                "to another device."
            )
        }


    # -----------------------------------------------------
    # SUCCESS
    # -----------------------------------------------------

    return {
        "ok": True,
        "message": "License approved.",
        "name": data.get("name", "USER"),
        "key": key,
        "expiry": expiry,
        "app_id": APP_ID
    }


# =========================================================
# HTTP SERVER
# =========================================================

class LicenseHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):

        print(
            "[HTTP]",
            self.address_string(),
            "-",
            format % args
        )


    def do_GET(self):

        if self.path == "/":

            send_json(
                self,
                200,
                {
                    "ok": True,
                    "service": APP_ID,
                    "status": "online"
                }
            )

            return


        if self.path == "/health":

            send_json(
                self,
                200,
                {
                    "ok": True,
                    "status": "online"
                }
            )

            return


        send_json(
            self,
            404,
            {
                "ok": False,
                "message": "Not found."
            }
        )


    def do_POST(self):

        if self.path != "/check-key":

            send_json(
                self,
                404,
                {
                    "ok": False,
                    "message": "Endpoint not found."
                }
            )

            return


        try:

            content_length = int(
                self.headers.get(
                    "Content-Length",
                    "0"
                )
            )


            if content_length <= 0:

                send_json(
                    self,
                    400,
                    {
                        "ok": False,
                        "message": "Empty request."
                    }
                )

                return


            if content_length > 10000:

                send_json(
                    self,
                    413,
                    {
                        "ok": False,
                        "message": "Request too large."
                    }
                )

                return


            body = self.rfile.read(
                content_length
            )


            payload = json.loads(
                body.decode("utf-8")
            )


            if not isinstance(payload, dict):

                raise ValueError(
                    "Invalid JSON object"
                )


            result = check_license(
                payload
            )


            if result.get("ok"):

                send_json(
                    self,
                    200,
                    result
                )

            else:

                send_json(
                    self,
                    403,
                    result
                )


        except json.JSONDecodeError:

            send_json(
                self,
                400,
                {
                    "ok": False,
                    "message": "Invalid JSON."
                }
            )


        except Exception as e:

            print(
                "[SERVER ERROR]",
                repr(e)
            )

            send_json(
                self,
                500,
                {
                    "ok": False,
                    "message": "Server error."
                }
            )


# =========================================================
# START
# =========================================================

def main():

    print()
    print("=" * 45)
    print("        RIPON-MANGO LICENSE SERVER")
    print("=" * 45)
    print()

    print("[+] Firebase     : CONNECTED")
    print("[+] Application  :", APP_ID)
    print("[+] Host         :", HOST)
    print("[+] Port         :", PORT)
    print()

    print("[+] Server started...")
    print("=" * 45)
    print()


    server = HTTPServer(
        (HOST, PORT),
        LicenseHandler
    )


    try:

        server.serve_forever()

    except KeyboardInterrupt:

        print()
        print("[!] Server stopped.")

    finally:

        server.server_close()


if __name__ == "__main__":
    main()
