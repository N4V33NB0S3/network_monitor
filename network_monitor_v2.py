import os
import requests
import time
import sys

# Telegram Bot credentials
BOT_TOKEN = "redacted"
CHAT_ID = "redacted"
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# File to store downtime timestamp
DOWNTIME_LOG = "/tmp/network_downtime.log"

# Number of failed checks before confirming downtime
CHECK_COUNT = 3
CHECK_INTERVAL = 10  # Seconds between consecutive checks

def is_network_up():
    hostname = "8.8.8.8"
    for _ in range(CHECK_COUNT):
        response = os.system(f"ping -c 3 {hostname} > /dev/null 2>&1")
        if response == 0:
            return True
        time.sleep(CHECK_INTERVAL)  # Wait before retrying
    return False

def send_telegram_message(message):
    try:
        payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
        response = requests.post(TELEGRAM_URL, json=payload, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
    except Exception as e:
        print(f"Failed to send Telegram message: {e}", file=sys.stderr)

def log_downtime():
    try:
        with open(DOWNTIME_LOG, "w") as f:
            f.write(str(time.time()))
    except Exception as e:
        print(f"Failed to log downtime: {e}", file=sys.stderr)

def get_downtime_duration():
    try:
        if os.path.exists(DOWNTIME_LOG):
            with open(DOWNTIME_LOG, "r") as f:
                start_time = float(f.read())
            return time.time() - start_time
    except Exception as e:
        print(f"Failed to read downtime log: {e}", file=sys.stderr)
    return 0

def main():
    network_status = is_network_up()

    if not network_status:
        if not os.path.exists(DOWNTIME_LOG):
            print("Network is down - logging downtime")
            log_downtime()
    elif network_status and os.path.exists(DOWNTIME_LOG):
        downtime_duration = get_downtime_duration()
        minutes = int(downtime_duration // 60)
        seconds = int(downtime_duration % 60)
        message = f"✅ *Internet Restored!* Downtime lasted {minutes} min {seconds} sec."
        print(message)
        send_telegram_message(message)
        try:
            os.remove(DOWNTIME_LOG)
        except Exception as e:
            print(f"Failed to remove downtime log: {e}", file=sys.stderr)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)
