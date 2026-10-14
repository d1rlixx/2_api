import os
from dotenv import load_dotenv
import requests
import argparse


def get_conversion_result(exchangerate_token, base_code, target_code, amount):
    try:
        url = f"https://v6.exchangerate-api.com/v6/{exchangerate_token}/pair/{base_code}/{target_code}/{amount}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["conversion_result"]
    except requests.get as err:
        print(f'Ошибка HTTP: {err}')
        print(f'Код ответа: {response.status_code}')

def main():
    load_dotenv()
    exchangerate_token = os.getenv("EXCHANGERATE_TOKEN")
    parser = argparse.ArgumentParser(description='Конвертор валют')
    parser.add_argument('--base_code', type=str, default="RUB", help='Введите код базовой валюты(например, RUB):')
    parser.add_argument('--target_code', type=str, default="USD", help='Введите код целевой валюты(например, USD):')
    parser.add_argument('--amount', type=float, default=100000.0, help='Введите сумму: ')
    args = parser.parse_args()
    base_code = args.base_code.upper()
    target_code = args.target_code.upper()
    amount = args.amout
    conversion_result = get_conversion_result(exchangerate_token, base_code, target_code, amount)
    print(f"Результат конвертации: {conversion_result} {target_code}")


if __name__ == "__main__":
    main()