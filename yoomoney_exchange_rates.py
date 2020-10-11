from requests_html import HTMLSession
import re
import json
import sys

def main():
    session = HTMLSession()
    r = session.get("https://money.yandex.ru/account/exchange-rates")
    # json containing exchange rates is inlined in script element on the page,
    # so look only for elements without src attribute
    scripts = filter(lambda element: "src" not in element.attrs, r.html.find("script"))
    for s in scripts:
        # find js objects: {"currencyCode": "USD", ...}
        objects = re.findall("({[^{]+?})", s.full_text)
        # there are many js objects, we only need those with currency exhcnage rates
        objects = list(filter(lambda o: "currencyCode" in o and "buyRate" in o, objects))
        if objects:
            break
    if not objects:
        sys.exit(1)
    print(f"{'CURRENCY':<10} {'BUYRATE':<10} {'SELLRATE':<10}")
    for o in objects:
        exchange_data = json.loads(o)
        print(f"{exchange_data['currencyCode']:<10} {exchange_data['buyRate']:<10} {exchange_data['sellRate']:<10}")



if __name__ == "__main__":
    main()
