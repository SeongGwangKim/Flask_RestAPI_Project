import requests
import json

# temp.jpg
# sunny.png
post_data = [ {"origin": "sunny.png"} ]

url01 = 'http://127.0.0.1:5000/transimage'
url02 = 'http://127.0.0.1:5000/plussimage'

response = requests.post(url01, json=post_data)

print(response)
json_data = json.loads(response.text)
print(response.json())
print(json_data.get("results"))
print(type(json_data))