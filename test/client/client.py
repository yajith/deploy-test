import requests
import time
import os

SERVER_URL = os.environ.get('SERVER_URL', 'http://localhost:5000/ping')
CLIENT_ID = os.environ.get('CLIENT_ID', 'default_id')

while True:
    try:
        requests.post(SERVER_URL, json={'client_id': CLIENT_ID})
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(5)
