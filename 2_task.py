class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def weight(self, tolch):
        norm = 25  # кг\см
        mass = self.__width * self.__length * norm * tolch / 1000  #тонн
        return(mass)


way = Road(1500, 6)

print(way.weight(3))

