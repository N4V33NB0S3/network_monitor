# 🌐 Network Monitor Bot  
*Get Telegram alerts when your internet connection drops or recovers!*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Telegram-Bot-26A5E4?logo=telegram" alt="Telegram">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</p>

---

## 🚀 **Quick Start**
### 1. **Prerequisites**
- Python 3.8+
- Telegram bot token (get from [@BotFather](https://t.me/BotFather))
- `requests` library

```bash
pip install requests
```
### 2. **Configure the Script**
Edit these lines in network_monitor.py:
```
BOT_TOKEN = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"  # From BotFather
CHAT_ID = "-1001234567890"  # Get from @userinfobot
```
### 3. **Run as a Service (Linux)**

```
# Copy service file
sudo cp network_monitor.service /etc/systemd/system/

# Enable and start
sudo systemctl enable --now network_monitor
```
## 🔧 Customization
**Change Check Interval**
```
time.sleep(60)  # Edit seconds (e.g., 120 for 2 minutes)
```
### Add Email Notifications
```
import smtplib
def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@gmail.com", "app_password")
    server.sendmail("from@example.com", "to@example.com", "Subject: Network Alert\n\nInternet is down!")
```
## 📂 Files
```
network_monitor/
├── network_monitor.py       # Main script
├── network_monitor.service  # Systemd config
├── assets/                  # Images/GIFs
└── README.md                # This file
```
## ❓ FAQ
Q: How to get CHAT_ID?
A: Send /start to @userinfobot on Telegram.

Q: Service fails to start?
```
journalctl -u network_monitor -f  # Check logs
```
---
## 📜 License
**MIT © [Naveen Bose]**
<p align="left">
<img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</p>

