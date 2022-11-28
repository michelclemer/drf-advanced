import requests


endpoint = "http://127.0.0.1:8000/api/products/delete/2"

resp = requests.delete(endpoint)

print(resp.content)