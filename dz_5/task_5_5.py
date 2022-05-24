def get_uniq_numbers(src: list):
    uniq_numbers = set()
    src_set = set()
    uniq_numbers_list = []
    for el in src:
        if el not in src_set:
            uniq_numbers.add(el)
        else:
            uniq_numbers.discard(el)
        src_set.add(el)
    for number in src:
        if number in uniq_numbers:
            uniq_numbers_list.append(number)
    return uniq_numbers_list

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))