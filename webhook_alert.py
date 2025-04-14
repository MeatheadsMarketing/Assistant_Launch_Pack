"""
webhook_alert.py – Assistant Launch Pack v1.4

Sends external alerts via POST webhook.
Useful for:
- Notifications on flow completion
- Budget breaches
- Feedback triggers
"""

import requests
import json
from datetime import datetime
import os

WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://your-webhook-url.com")

def send_alert(message, level="info"):
    payload = {
        "text": f"[{level.upper()}] {datetime.utcnow().isoformat()} - {message}"
    }

    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 200:
            print("✅ Alert sent.")
        else:
            print(f"❌ Alert failed ({response.status_code}):", response.text)
    except Exception as e:
        print("❌ Alert exception:", str(e))

# Example usage
if __name__ == "__main__":
    send_alert("Test alert from Assistant Launch Pack", level="info")
