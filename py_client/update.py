import requests


endpoint = "http://127.0.0.1:8000/api/products/update/1/"


data = {
    "title": "Titulo mudado no update do client com classe diferente2s"
}

resp = requests.put(endpoint, json=data)

print(resp.json())