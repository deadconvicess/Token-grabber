# 🛡️ Secure Token Logger (Educational Use Only)

> ⚠️ **Disclaimer**: This project is intended strictly for **educational**, **research**, and **cybersecurity awareness** purposes. Do **not** use this code for unethical or illegal activities. The author does not condone misuse of this code in any way.

---

## 🚀 Overview

This project demonstrates how Discord token loggers might work. It simulates how local tokens are discovered and exfiltrated, allowing developers and security professionals to understand the risk and build effective defenses.

### 🔍 Why Use This?

- To understand the **inner workings** of malicious token-stealing scripts.
- For learning how to **detect, mitigate, or prevent** similar threats.
- As an **educational example** of Windows-based scripting and encryption.

---

## 🧠 Features

- 🔐 Token decryption via local master key
- 📦 Extracts Discord tokens from Chromium-based browsers
- ⚙️ Built-in anti-debug and VM detection
- 📤 Simulates data exfiltration via webhook
- 🧪 AES encryption demonstration
- 🖥️ Grabs basic system/user info (for testing)

---

## ⚙️ Installation

### ✅ Requirements

- Python 3.8 or higher
- Windows OS

### 📦 Dependencies

Install via pip:

```bash
pip install pycryptodome pyperclip pillow pypiwin32


🛠️ Usage
⚠️ Use in a controlled test environment or sandbox.

Replace the webhook placeholder in main.py:

python
Copy
Edit
WEBHOOK_URL = "https://your.webhook.here"
Run the script:

bash
Copy
Edit
python main.py
The script will gather local Discord tokens (if available) and simulate sending them to your test webhook.

📁 Project Structure
bash
Copy
Edit
.
├── main.py         # Main script (educational simulation)
├── README.md       # This file
🧪 Educational Goals
Teach how Discord token loggers operate

Raise awareness about sensitive local storage handling

Demonstrate token encryption and decryption

Help developers defend against such threats

❗ Legal Notice
This code is provided as-is for research and educational purposes. The author is not responsible for any misuse. Unauthorized access, data collection, or deployment of this code without consent is illegal.

📎 License
This project is licensed under the MIT License.

🧠 Credits
Created by deadconvicess for demonstration and ethical awareness purposes.

Want to learn more about token security? Check out:

Discord Developer Docs

OWASP Top 10

yaml
Copy
Edit

---

### ✅ To Use It:
- Save this as `README.md` in your repository.
- GitHub will render it nicely with icons and sections.

Would you like a **banner image** or **GitHub badges** added to this for even more polish?
