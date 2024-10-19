# This is third party application that is used to request the api and the  api gives the response. 
import requests

URL = "http://127.0.0.1:8000/stuinfo/2"

r = requests.get(url = URL)

data = r.json()

print(data)