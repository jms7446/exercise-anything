import os
import sys
import json

import requests

url = 'https://openapi.naver.com/v1/search/blog?query=윤웅식'
client_id = "VYduiIsjYM4mHHh9mtOa"
client_secret = 'mG7dFMwrZv'
headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret,
}

r = requests.get(url, headers=headers)
for d in json.loads(r.text)['items']:
    print(d)
