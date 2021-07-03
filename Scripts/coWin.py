import requests

x = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=832108&date=21-05-2021')

xjson = x.json()

print(xjson[])