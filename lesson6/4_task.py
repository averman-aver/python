
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def not_police(self):
        if self.is_police == False:
            return ('{} is not a police car'.format(self.name))

    def go(self):
        return ('{} is started'.format(self.name))

    def stop(self):
        return ('{} is stopped'.format(self.name))


    def turn_right(self):
        return ('{} is turned right'.format(self.name))

    def turn_left(self):
        return ('{} is turned left'.format(self.name))

    def show_speed(self):
        return ('Current speed of {} is {}'.format(self.name, self.speed))



class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            #return f'Speed of {self.name} is higher than allow for town car'
            print('   !!!Speed of {} is too high!!!'.format(self.name))
        return ('Current speed of {} {} is {}'.format('Towncar', self.name, self.speed))

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('   !!!Speed of {} is too high!!!'.format(self.name))
        return ('Current speed of {} {} is {}'.format('Workcar', self.name, self.speed))


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return ('{} is a police car'.format(self.name))
        else:
            return ('{} is not a police car'.format(self.name))

e_mobil = Car(90, 'White', 'Ё-мобиль', False)
ferrari = SportCar(150, 'Red', 'Ferrari', False)
smart = TownCar(61, 'White', 'Smart', False)
gazel = WorkCar(70, 'Gray', 'Газель', True)
ford = PoliceCar(100, 'White-Blue', 'Ford', True)

print(e_mobil.go())
print(e_mobil.stop())
print(e_mobil.turn_right())
print(e_mobil.not_police())
print(smart.turn_left())
print(ferrari.not_police())
print(ferrari.show_speed())
print(smart.show_speed())
print(ford.police())
print(ford.show_speed())
print('Color of {} {} is {}'.format(ford.police(), ford.name, ford.color))
