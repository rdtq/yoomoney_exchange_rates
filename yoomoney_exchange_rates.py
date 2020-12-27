import urllib.request
import re
import json
import sys
from datetime import datetime

def main():
    with urllib.request.urlopen("https://yoomoney.ru/account/exchange-rates") as f:
        text = f.read().decode("utf8")
    # find possible js objects: {"currencyCode": "USD", ...}
    objects = re.findall("({[^{]+?})", text)
    # there are many js objects, we only need those with currency exhcnage rates
    objects = list(filter(lambda o: "currencyCode" in o and "buyRate" in o, objects))
    if not objects:
        sys.exit(1)
    for o in objects:
        exchange_data = json.loads(o)
        with open(f"{exchange_data['currencyCode']}.txt", "a") as write_file:
            write_file.write(f"{datetime.utcnow().isoformat()} {exchange_data['buyRate']} {exchange_data['sellRate']}\n")



if __name__ == "__main__":
    main()
