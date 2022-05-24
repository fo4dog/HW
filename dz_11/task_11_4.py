class Sklad:
    def __init__(self):
        self.sklad_dict = {}

    def add_to(self, equipment):
        self.sklad_dict.setdefault(equipment.group, []).append(equipment)

    def extract(self, group):
        if self.sklad_dict[group]:
            self.sklad_dict.setdefault(group).pop(0)
            print(f"Со склада забрали {group}")


class OfficeEquipment:
    def __init__(self, maker, model):
        self.maker = maker
        self.model = model
        self.group = self.__class__.__name__


    def __repr__(self):
        return f'{self.maker}-{self.model}'


class Printer(OfficeEquipment):
    def __init__(self, maker, model, paper_type, printer_type):
        super().__init__(maker, model)
        self.paper_type = paper_type
        self.printer_type = printer_type

    def to_print(self):
        return f"Принтер начал печать"

    def __repr__(self):
        return f'Производитель: {self.maker}, модель: {self.model}, тип бумаги: {self.paper_type},' \
               f' тип принтера: {self.printer_type}'


class Monitor(OfficeEquipment):
    def __init__(self, maker, model, diagonal, matrix_type):
        super().__init__(maker, model)
        self.diagonal = diagonal
        self.matrix_type = matrix_type

    def to_work(self):
        return f"Монитор включен"

    def __repr__(self):
        return f'Производитель: {self.maker}, модель: {self.model}, диагональ: {self.diagonal},' \
               f' тип монитора: {self.matrix_type}'


if __name__ == "__main__":
    sklad = Sklad()
    printer = Printer("hp", "Ink Tank 115", "A4", "laser")
    monitor = Monitor("samsung", "F24T350FHI IPS", "23.8", "matrix")
    hp_monitor = Monitor("hp", "EliteDisplay E243p", "23.8", "matrix")
    sklad.add_to(printer)
    sklad.add_to(monitor)
    sklad.add_to(hp_monitor)
    print(sklad.sklad_dict)
    sklad.extract('Monitor')
    print(sklad.sklad_dict)
