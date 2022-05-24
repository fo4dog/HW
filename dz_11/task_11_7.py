class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary < 0:
            return f"Z = {self.real} {self.imaginary}i"
        elif self.imaginary == 0:
            return f"Z = {self.real}"
        else:
            return f"Z = {self.real} + {self.imaginary}i"

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        if imaginary < 0:
            return f"Сумма комплексных чисел равна: {real} {imaginary}i"
        elif imaginary == 0:
            return f"Сумма комплексных чисел равна: {real}"
        else:
            return f"Сумма комплексных чисел равна: {real} + {imaginary}i"

    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        if imaginary < 0:
            return f"Разность комплексных чисел равна: {real} {imaginary}i"
        elif imaginary == 0:
            return f"Разность комплексных чисел равна: {real}"
        else:
            return f"Разность комплексных чисел равна: {real} + {imaginary}i"

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        if imaginary < 0:
            return f"Произведение комплексных чисел равна: {real} {imaginary}i"
        elif imaginary == 0:
            return f"Произведение комплексных чисел равна: {real}"
        else:
            return f"Произведение комплексных чисел равна: {real} + {imaginary}i"



if __name__ == "__main__":
    complex_numder_1 = ComplexNumber(4, -2)
    complex_numder_2 = ComplexNumber(3, 1)
    print(complex_numder_1)
    print(complex_numder_2)
    print(complex_numder_1 + complex_numder_2)
    print(complex_numder_1 - complex_numder_2)
    print(complex_numder_1 * complex_numder_2)