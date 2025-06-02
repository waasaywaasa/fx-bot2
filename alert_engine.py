import requests

# Replace with your actual Telegram bot token and chat ID
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": f"📢 Fx Bot2.0 Alert: {message}"}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Failed to send alert:", e)