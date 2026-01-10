import requests

LOGIC_APP_URL = "https://prod-17.centralindia.logic.azure.com:443/workflows/0b44b6ac7a2b47b8a1b907b6c01e7888/triggers/When_an_HTTP_request_is_received/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2FWhen_an_HTTP_request_is_received%2Frun&sv=1.0&sig=Dv_saqKlitfU0THr9c_aU_r3npp6hLEKrPZY0ib50uA"

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
