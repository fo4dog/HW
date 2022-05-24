def odd_nums(number: int):
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    nums_gen = (num for num in range(1, number+1, 2))
    return nums_gen

n = 15
generator = odd_nums(n)
print(*generator) # Если нужен переход на новую строку, то дописать sep = "\n"
