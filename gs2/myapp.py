import requests
import json
URL = "http://127.0.0.1:8000/stucreate/"

data = {
        'name': 'Mukesh',
        'roll' : 101,
        'city' : 'Khalilabad'
}

json_data = json.dumps(data)

result = requests.post(url = URL, data = json_data)
data = result.json()

print(data)
