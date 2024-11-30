import requests

response = requests.get('http://127.0.0.1:8000/api/books/')
if response.status_code == 200:
    print("API Response:", response.json())
else:
    print("Failed to fetch data:", response.status_code)
