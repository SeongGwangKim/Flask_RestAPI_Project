import requests
import json

# temp.jpg
# sunny.png
post_data = [ { "origin": "temp.jpg" } ]

url = 'http://127.0.0.1:5000/esrganimage'


response = requests.post(url, json=post_data)
print(response)
json_data = json.loads(response.text)
print(response.json())
print(json_data.get("results"))
print(type(json_data))