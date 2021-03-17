import requests
import json

while(True):
    text = input('Enter Text: ')
    res = requests.post('http://localhost:5005/webhooks/rest/webhook', data='{"message": "'+text.strip()+'"}')
    print(res.json()[0]['text'])