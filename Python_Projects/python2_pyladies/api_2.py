import requests

stranka = requests.get('http://thecatapi.com/api/images/get?format=src&type=gif')
stranka.raise_for_status()

print(stranka.status_code)