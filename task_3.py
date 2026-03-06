import requests
import json

url = "https://www.cbr-xml-daily.ru/daily_json.js"

def get_exchange_rates():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['Valute']
    else:
        return None

def create_currency_groups(currencies):
    groups = {}
    for currency in currencies:
        code = currency['CharCode']
        groups[code] = []
    return groups

def add_currency_to_group(groups, currency):
    code = currency['CharCode']
    groups[code].append(currency)

def save_currency_groups(groups, filename):
    with open(filename, 'w') as file:
        json.dump(groups, file, indent=4)

def load_currency_groups(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def main():
    currencies = get_exchange_rates()
    if currencies is None:
        print("Ошибка при получении курса валют.")
        return

    groups = create_currency_groups(currencies)

    for currency in currencies:
        add_currency_to_group(groups, currency)

    save_currency_groups(groups, 'save.json')

    loaded_groups = load_currency_groups('save.json')
    print("Считанные группы валют:")
    print(loaded_groups)


main()
