import utils


if __name__ == "__main__":
    kurs, date_value = utils.currency_rates_adv("USD")
    print(kurs, date_value)
    kurs, date_value = utils.currency_rates_adv("EUR")
    print(kurs, date_value)
    kurs, date_value = utils.currency_rates_adv("AUD")
    print(kurs, date_value)

"""
Многострочным коментарием выдавало ошибку, поэтому сделал так
"""
# C:\Users\72499\OneDrive\Desktop\HW\dz_4>python task_4_4.py
# 81.288 2022-04-14
# 88.0024 2022-04-14
# 60.6246 2022-04-14

