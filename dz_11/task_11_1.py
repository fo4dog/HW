import datetime
from datetime import date


class Data:
    def __init__(self, data):
        self.data = data.split('.')

    @classmethod
    def type(cls, data):
        try:
            int(data.split('.')[0]), int(data.split('.')[1]), int(data.split('.')[2])
        except ValueError:
            return "Неверно указана дата"
        else:
            return "Дата указана верно"

    @staticmethod
    def valid_date(data):
        lst_date = data.split('.')
        try:
            date(int(lst_date[2]), int(lst_date[1]), int(lst_date[0]))
        except:
            return "Такой даты не существует"
        else:
            return "Есть такая дата"


if __name__ == '__main__':
    input_data = '09.05.2002'
    print(Data.valid_date(input_data))
    print(Data.type(input_data))
