
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return ('Запуск отрисовки')
class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return ('Линия')

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return ('Штрих')

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return ('След')

koh_i_noor = Pencil('Koh-i-Noor')
lamy = Pen('Lamy')
job = Handle('JOB')
print('{} рисует {}'.format(koh_i_noor.title, koh_i_noor.draw()))
print('Ручка {} оставляет {}, а маркер {} - {}'.format(lamy.title, lamy.draw(), job.title, job.draw()))