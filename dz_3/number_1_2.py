def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """
    dict_of_numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять'}
    str_out = None
    if value in dict_of_numbers.keys():
        str_out = f'{dict_of_numbers.get(value)}'
    elif value.lower() in dict_of_numbers.keys() and value == value.title():
        str_out = f'{(dict_of_numbers.get(value.lower())).title()}'
    return str_out


print(num_translate_adv("One"))
print(num_translate_adv("two"))