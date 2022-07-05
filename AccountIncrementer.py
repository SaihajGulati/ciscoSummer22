import requests

API_KEY = "4f61628d-012e-4536-b3d0-c136faa911fd"
URL = "https://restapi20.jasper.com/rws/api/v1/accounts"

r = requests.get(url = URL)

data = r.json()