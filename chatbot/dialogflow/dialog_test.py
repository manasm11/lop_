import requests
import json
url = 'https://dialogflow.clients6.google.com/v2beta1/projects/repair-service-dota/locations/global/agent/sessions/cc05926b-a00b-4ab2-b082-9010032d6e21:detectIntent'
payload = {
    "queryInput": {
        "text":{
            "text": "Book an appointment for tomorrow",
            "languageCode":"en"
            }
        },"queryParams":{
            "source":"DIALOGFLOW_CONSOLE",
            "timeZone":"Asia/Calcutta"
            }
        }
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer ya29.A0AfH6SMBMR-QQw4di16swEmXqIPc9sKIQi1Gx-HVy53L4bW_HHPFvliNl_-wiD-5PrU4gF0OdyhsOXQmFpU31BTIPr2eDpTy-cZH-nUtv2S6WZM-geHraEvWzkzdUNTGEo2b_RqD0EunMgyGSio6AZ97F2El7YjYS-vXl2wDcc71Buvt5IX4-2ZWBb-k3_beXWyypAaWYyY58YWdtUcbYDDH9Pg_hmqjLHFWrgYzWcz07qLI"
    }

r = requests.post(url, data=json.dumps(payload), headers=headers)
print(json.dumps(r.json(), indent=1))