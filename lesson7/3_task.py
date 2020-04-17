
class Cell:
    def __init__(self, cells_number):
        self.cells_number = int(cells_number)

    def __str__(self):
        return (f'Клетка {self.cells_number * "*"}')

    def __add__(self, other):
        return Cell(self.cells_number + other.cells_number)

    def __sub__(self, other):
        if (self.cells_number - other.cells_number) > 0:
            return Cell(int(self.cells_number - other.cells_number))
        else:
            return ("Ошибка")

    def __mul__(self, other):
        return Cell(int(self.cells_number * other.cells_number))

    def __truediv__(self, other):
        return Cell(round(self.cells_number / other.cells_number))


    def make_order(self, cells_in_line):
        line = ''
        for i in range(self.cells_number // cells_in_line):
            line += f'{"*" * cells_in_line}' + '\\n'
        line += f'{"*" * (self.cells_number % cells_in_line)}'
        return line

cells1 = Cell(3)
cells2 = Cell(12)

print('+', cells1 + cells2)
print('-', cells1 - cells2)
print('-', cells2 - cells1)
print('*', cells1 * cells2)
print('/', cells2 / cells1)

print(cells1.make_order(7))
print(cells2.make_order(7))

