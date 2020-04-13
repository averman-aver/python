class TrafficLight:
    def __init__(self, color):
        self.color = color

    def running(self):
        if self.color == 'on':
            import time
            self.color = 'Красный'

            print('Вкл.')
            print(self.color)
            time.sleep(7)

            self.color = 'Желтый'
            print(self.color)
            time.sleep(2)

            self.color = 'Зеленый'
            print(self.color)
            time.sleep(7)
            print('Выкл')

run = TrafficLight('on')
run.running()