import sys
import utils



if __name__ == '__main__':
    kurs, date_value = utils.currency_rates_adv(sys.argv[1])
    print(kurs, date_value)