from urllib import response
import requests

address = 'http://10.0.1.83:5000'

response = requests.get(address)

print(response.text)