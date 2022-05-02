import datetime
import requests
import decimal

def currency_rates_adv(code: str):
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    r = requests.get(url).text
    resp = r.split(code)
    value = 0
    date_kurs = 0

    if len(resp) == 1:
        value = 'Такой валюьы не обнаружено'
        date_kurs = 'Дата для несуществующей валюты не может быть найдена'
    else:
        value = resp[1].split("<Value>")[1].split("</Value>")[0]
        value = float(value.replace(",", ".")) # курс валюты float
        # value = decimal.Decimal(value.replace(",", "."))  # курс валюты Decimal
        date_kurs = requests.get(url).headers["Date"]
        date_kurs = datetime.datetime.strptime(date_kurs, "%a, %d %b %Y %H:%M:%S GMT").date()
    return value, date_kurs

kurs, date_value = currency_rates_adv("EUR")


print(kurs, date_value)