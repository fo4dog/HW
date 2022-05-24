class NumbersInList(Exception):
    def __init__(self):
        pass


if __name__ == "__main__":
    list_of_numbers = []
    while True:
        numb = input()
        if numb == "pass":
            break
        try:
            if not numb.isdigit():
                raise NumbersInList
        except NumbersInList:
            print("Вы должны ввести число, а не строку")
        else:
            list_of_numbers.append(int(numb))
    print(f"Ваш список: {list_of_numbers}")