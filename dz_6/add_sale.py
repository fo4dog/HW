import csv
import sys

def add_sale(price: float):
    with open('bakery.csv', 'a+', encoding='utf-8') as fw:
        writer = csv.writer(fw, delimiter = ",", lineterminator="\r")
        writer.writerow([price])

if __name__ == '__main__':
    add_sale(float(sys.argv[1]))