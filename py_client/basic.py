import requests


endpoint = "http://127.0.0.1:8000/api/"

resp = requests.post(endpoint, json={"titles": "Hello world", "title": "None", "price": 1.90})
print(resp.headers)
#print(resp.text)
print(resp.json())