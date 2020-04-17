
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, v, h):
        self.v = v
        self.h = h
    @abstractmethod
    def sq(self):
        sq_clothes = self.v * self.h  # пример, без физического смысла
        return(sq_clothes)

class Coat(Clothes):
    def __init__(self, v, h=0):
        super().__init__(v, h)

    def sq(self):
        sq_coat = round(self.v/6.5 + 0.5, 2)
        return (sq_coat)

class Suit(Clothes):
    def __init__(self, h, v=0):
        super().__init__(v, h)

    def sq(self):
        sq_suit = round(2 * self.h + 0.3, 2)
        return (sq_suit)

class Textil(Clothes):
    def __init__(self, v, n, h, m):
        super().__init__(v, h)
        self._n = n  # кол-во Coat
        self.m = m  # кол-во Suit
    @property
    # def get_number_n(self):
    def n(self):
        self._n = int(self._n)
        # return(self._n)  # вариант более подходящий под задание
        return(self)

    def sq(self):
        # sq = round(self.v/6.5 + 0.5, 2) * self.n + round(2 * self.h + 0.3, 2) * self.m
        sq = Coat.sq(self) * self._n + Suit.sq(self) * self.m
        return (f'Суммарная площадь ткани {sq} метров квадратных')

my_coat = Coat(52)
print(my_coat.sq())

my_suit = Suit(3)
print(my_suit.sq())

my_garederob = Textil(52, 10, 3, 11)
print(my_garederob.sq())

my_garederob = Textil(52, '10', 3, 11)
print(type(my_garederob.n), my_garederob.n)
a = my_garederob.n
#a = my_garederob.get_number_n()
print(a.sq())  # работает только в варианте return(self) в def n(self)
print((my_garederob.n).sq())  # работает только в варианте return(self) в def n(self)