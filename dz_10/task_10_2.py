class Clothes:
    @property
    def calculate(self):
        return 0


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
    def calculate(self):
        return f'Сумма затраченной ткани равна: {self.size / 6.5 + 0.5:.2f}'


class Costume(Clothes):
    def __init__(self, height):
        self.height = height
    def calculate(self):
        return f'Сумма затраченной ткани равна: {2 * self.height + 0.3 :.2f}'


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate())  # 7.42
    print(costume.calculate())  # 6.3
