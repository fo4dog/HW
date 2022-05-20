class Cell:

    def __init__(self, cells: int):
        self.cells = cells

    def __add__(self, other):
        if isinstance(other, Cell):
            cells = self.cells + other.cells
            return Cell(cells)
        else:
            raise TypeError("действие допустимо только для экземпляров того же класса")

    def __sub__(self, other):
        if isinstance(other, Cell):
            cells = self.cells - other.cells
            if cells <= 0:
                raise ValueError("недопустимая операция")
            return Cell(cells)
        else:
            raise TypeError("действие допустимо только для экземпляров того же класса")

    def __mul__(self, other):
        if isinstance(other, Cell):
            cells = self.cells * other.cells
            return Cell(cells)
        else:
            raise TypeError("действие допустимо только для экземпляров того же класса")

    def __truediv__(self, other):
        if isinstance(other, Cell):
            cells = self.cells // other.cells
            return Cell(cells)
        else:
            raise TypeError("действие допустимо только для экземпляров того же класса")

    def __floordiv__(self, other):
        if isinstance(other, Cell):
            cells = self.cells / other.cells
            return Cell(round(cells))
        else:
            raise TypeError("действие допустимо только для экземпляров того же класса")

    def make_order(self, number: int) -> str:
        out = ''
        for i in range(self.cells // number):
            out += '*' * number + '\n'
        out += '*' * (self.cells % number) + '\n'
        return out


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))
    """
    **********
    *****
    """

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    """
    ******
    ******
    *
    """

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    """
    ******
    ******
    """

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)  # 30

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)  # 3

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)  # 1

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)  # недопустимая операция

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)  # действие допустимо только для экземпляров того же класса