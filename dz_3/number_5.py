import random # библиотека random

# Списки из которых формируются шутки
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """
    Возвращает список шуток в количестве count
    :param count: int | количество шуток
    :return list | список шуток
    """
    list_out = []  # список шуток
    for i in range(count): # цикл длинной count создающий шутки
        list_out.append(f"{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}") # создание 1 шутки
    return list_out


print(get_jokes(2))
print(get_jokes(10))

# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
def get_jokes_adv(count: int, flag=True) -> list:
    """
    Возвращает список шуток в количестве count, если flag=True, то функция возвращает список, в котором нет повторяющихся слов,
    в случае если flag=True и количество слов из которых создается список меньше заданного числа шуток выведется:
     ['Количество шуток превышает количество слов, поэтому не возможно составить шутки без повторений']
    :param count: int | количество шуток
    :param flag: bool | Повторяются слова или нет
    :return: list | список шуток
    """
    list_out = []
    if count > len(nouns) and flag is True:
        list_out = ['Количество шуток превышает количество слов, поэтому не возможно составить шутки без повторений']
    elif flag is True:

        used_nouns = []
        used_adverbs = []
        used_adjectives = []
        for i in range(count):  # цикл длинной count создающий шутки
            random_noun = random.choice(nouns)
            random_adverbs = random.choice(adverbs)
            random_adjectives = random.choice(adjectives)
            while random_adjectives in used_adjectives or random_noun in used_nouns or random_adverbs in used_adverbs:
                if random_noun in used_nouns:
                    random_noun = random.choice(nouns)
                if random_adverbs in used_adverbs:
                    random_adverbs = random.choice(adverbs)
                if random_adjectives in used_adjectives:
                    random_adjectives = random.choice(adjectives)

            list_out.append(f"{random_noun} {random_adverbs} {random_adjectives}")
            used_nouns.append(random_noun)
            used_adverbs.append(random_adverbs)
            used_adjectives.append(random_adjectives)
    else:
        for i in range(count):  # цикл длинной count создающий шутки
            list_out.append(f"{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}")  # создание 1 шутки

    return list_out

print(get_jokes_adv(2))
print(get_jokes_adv(5))
print(get_jokes_adv(10, flag=False))