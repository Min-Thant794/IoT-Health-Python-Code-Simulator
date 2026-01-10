import time
import json
import random
import os
from dotenv import load_dotenv
from datetime import datetime, timezone
from azure.iot.device import IoTHubDeviceClient, Message
from alert_service import send_alert

load_dotenv()

CONNECTION_STRING = os.getenv("CONNECTION_STRING")

if not CONNECTION_STRING:
    raise ValueError("CONNECTION_STRING not found in .env file")

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

print("Connecting to Azure IoT Hub...")
client.connect()
print("Azure IoT Hub is successfully connected!")

last_alert_time = 0
ALERT_INTERVAL = 60

last_status = "NORMAL"

while True:

    current_time = time.time()

    data = {
        "heartRate": random.randint(60, 120),
        "spo2": random.randint(88, 100),
        "temperature": round(random.uniform(36.0, 39.0), 1),
        "eventTime": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    }

    if (
        data["heartRate"] > 120 or
        data["heartRate"] < 50 or
        data["spo2"] < 92 or
        data["temperature"] > 38 or
        data["temperature"] < 35.5
    ):
        status = "ABNORMAL"

        if current_time - last_alert_time >= ALERT_INTERVAL:
            print("Abnormal detected:", data)
            send_alert(data)
            last_alert_time = current_time

    else:
        status = "NORMAL"

    last_status = status
    data["status"] = status

    message = Message(json.dumps(data))
    message.content_encoding = "utf-8"
    message.content_type = "application/json"
    message.custom_properties["healthStatus"] = data["status"]

    try:
        client.send_message(message)
        print(f"Sending data to IoT Hub: {data}")
    except Exception as e:
        print("Error sending data:", e)

    time.sleep(10)