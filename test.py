'''



'''

class User:
    user_count = 0
    def __init__(self, name, age, adress, bonus, loyalty):
        self.name = name
        self.age = age
        self.adress = adress

        self.bonus = bonus
        self.loyalty = loyalty
        User.user_count += 1

    def add_bonus(self, bonus_count):
        self.bonus += bonus_count
        self.loyalty = self.bonus // 1000

        if self.loyalty >= 3:
            self.loyalty = 3
            print('Бонусный уровень покупателя {}: {}'.format(self.name, self.loyalty))




user1 = User('Ivan', 45, 'Moscow', 0, 0)
print(user1)

user2 = User('Masha', 34, 'Penza', 0, 0)
user2.add_bonus(10000)

#print(user1[:])
import time
print('Вкл')
time.sleep(3)
print('Выкл')

'''
4)Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните 
вызов методов и также покажите результат.

5)Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

'''
