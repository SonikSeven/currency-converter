import requests
import json


def get_rate(currency_1, currency_2):
    response = requests.get(f"http://www.floatrates.com/daily/{currency_1}.json")
    data = json.loads(response.text)
    return data[currency_2]["rate"]


def main():
    currency_1 = input().lower()
    cache = {}
    if currency_1 != "usd":
        cache["usd"] = get_rate(currency_1, "usd")
    if currency_1 != "eur":
        cache["eur"] = get_rate(currency_1, "eur")
    while True:
        currency_2 = input().lower()
        if not currency_2:
            return
        number = float(input())
        print("Checking the cache...")
        if currency_2 in cache:
            print("Oh! It is in the cache!")
        else:
            print("Sorry, but it is not in the cache!")
            cache[currency_2] = get_rate(currency_1, currency_2)
        result = round(number * cache[currency_2], 2)
        print(f"You received {result} {currency_2.upper()}.")


if __name__ == "__main__":
    main()
