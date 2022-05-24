class DevByZerro(Exception):
    pass


if __name__ == "__main__":
    try:
        first_num = int(input())
        second_num = int(input())
        if second_num == 0:
            raise DevByZerro
    except ValueError:
        print("Вы ввели не число")
    except DevByZerro:
        print("Деление на ноль")
