import requests

from getpass import getpass

session = requests.Session()

auth_endpoint = "http://127.0.0.1:8000/auth/"

username = ''
password = ''

tipo = int(input('user -> '))

if tipo == 1:
    username = 'root'
    password = 'root'
elif tipo == 2:
    username = 'staff'
    password = getpass()

auth_response = session.post(auth_endpoint, json={"username": username, "password": password})
print(auth_response.headers)
print(auth_response.json())


endpoint = "http://127.0.0.1:8000/api/products/"
headers = {
    'Authorization': f'Bearer {auth_response.json()["token"]}'
}

endpoint = "http://127.0.0.1:8000/api/products/"
data = {
    "title": "My title2",
    "price": 22.90
}


resp = requests.post(endpoint, json=data, headers=headers)

print(resp.content)