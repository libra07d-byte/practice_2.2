import requests

urls = [
    "https://github.com/",
    "https://www.binance.com/en",
    "https://tomtit.tomsk.ru/",
    "https://jsonplaceholder.typicode.com/",
    "https://moodle.tomtit-tomsk.ru/"
]

def check_url(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        if status_code == 200:
            print(f"{url} - доступность(доступен) - код ответа({status_code})")
        elif status_code == 404:
            print(f"{url} - доступность(не найден) - код ответа({status_code})")
        elif status_code == 500:
            print(f"{url} - доступность(вход запрещен) - код ответа({status_code})")
        else:
            print(f"{url} - доступность(неизвестно) - код ответа({status_code})")
    except requests.exceptions.RequestException as err:
        print(f"{url} - доступность(не доступен) - ошибка({err})")

for url in urls:
    check_url(url)
