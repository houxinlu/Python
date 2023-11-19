# request
import requests

r = requests.get("https://www.baidu.com")
print(r.text, r.status_code)
