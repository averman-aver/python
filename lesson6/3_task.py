'''
Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
 '''

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
     def __init__(self, name, surname, position, wage, bonus):
      super().__init__(name, surname, position, wage, bonus)

     def get_full_name(self):  # метод получения полного имени сотрудника
        full_name = "{} {}".format(self.name, self.surname)
        return (full_name)

     def get_total_income(self):  # метод получения дохода с учетом премии
        total_income = self._income['wage'] + self._income['bonus']
        return (total_income)
        #print(total_income)

        
worker1 = Position('Vasya', 'Petrov', 'engineer', 50000.00, 30000.01)
worker2 = Position('Petya', 'Vasiliev', 'manager', 60000.00, 30000.00)

print(worker1.get_full_name(), worker1.get_total_income())
print(worker1.get_total_income())
print(worker2.position)