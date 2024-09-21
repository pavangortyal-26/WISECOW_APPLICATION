import time
import requests

# URL of the application to monitor
APPLICATION_URL = 'http://example.com'

def check_application_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Application is UP. Status code: {response.status_code}")
        else:
            print(f"Application is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Application is DOWN. Error: {e}")

if __name__ == "__main__":
    while True:
        check_application_status(APPLICATION_URL)
        time.sleep(5)  # Check every 60 seconds
