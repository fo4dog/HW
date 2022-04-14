import requests
import decimal
from datetime import datetime


def currency_rates(code: str) -> float:
    """
    Фукнция находит курс валюты code  на сайте url
    :param code: str | Курс этой валюты нас интересует
    :return: value | Значение курса валюты
    """
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    r = requests.get(url).text
    r = r.split(code)
    if len(r) == 1:
        return None
    else:
        value = r[1].split("<Value>")[1].split("</Value>")[0]
        # value = float(value.replace(",", ".")) # курс валюты float
        value = decimal.Decimal(value.replace(",", "."))  # курс валюты Decimal
        return value


print("Курс доллара:", currency_rates("USD"))
print("Курс евро:", currency_rates("EUR"))
