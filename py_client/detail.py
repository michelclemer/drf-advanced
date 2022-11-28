import requests


endpoint = "http://127.0.0.1:8000/api/products/1"

resp = requests.get(endpoint)

print(resp.json())