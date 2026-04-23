import requests
import os
from dotenv import load_dotenv

load_dotenv()

LOGIC_APP_URL = os.getenv("LOGIC_APP_URL")

if not LOGIC_APP_URL:
    raise ValueError("LOGIC_APP_URL not found in .env file")


def send_alert(payload):
    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            LOGIC_APP_URL,
            json=payload,
            headers=headers,
            timeout=5
        )

        print("Alert sent to Logic App")
        print("Status code:", response.status_code)

    except Exception as e:
        print("Failed to send alert:", e)
