import urllib.request
import re
import json
import sys

def main():
    with urllib.request.urlopen("https://money.yandex.ru/account/exchange-rates") as f:
        text = f.read().decode("utf8")
    # find possible js objects: {"currencyCode": "USD", ...}
    objects = re.findall("({[^{]+?})", text)
    # there are many js objects, we only need those with currency exhcnage rates
    objects = list(filter(lambda o: "currencyCode" in o and "buyRate" in o, objects))
    if not objects:
        sys.exit(1)
    print(f"{'CURRENCY':<10} {'BUYRATE':<10} {'SELLRATE':<10}")
    for o in objects:
        exchange_data = json.loads(o)
        print(f"{exchange_data['currencyCode']:<10} {exchange_data['buyRate']:<10} {exchange_data['sellRate']:<10}")



if __name__ == "__main__":
    main()
