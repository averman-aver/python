#!/usr/bin/python3
import random
import sys          # для запуска системной остановки sys.exit(1) при завершении игры
import time         # использование задержки при выводе ответа о неправильном нажатии клавиш y/n


def gen():                                      # генератор номера бочонка. вынести предложил PyCharm
    cask_list = random.sample(range(1, 91), 90)
    for i, y in enumerate(cask_list):
        print(f'Бочонок {y} (осталось {90 - (i + 1)} шт)')
        yield y


class Cask:
    def __init__(self):
        self.cask_gen = gen()


class Lotto:
    def __init__(self):
        self.all_row = 6                        # формирование рядов для двух карт сразу
        self.set_card()
        self.score = 0
        self.name = ""

    def set_card(self):
        temp = []  # если вынести из функции наверх, то карточка компа не будет иметь совпадающие числа с картой игрока
        cards = []
        for i in range(6):
            nums = []
            while len(nums) < 5:
                el = str(random.randint(1, 90)) # <class 'str'>
                if el not in temp:              # проверка на повторяющиеся числа через временный список temp
                    nums.append(el)
                    temp.append(el)
            nums = list(nums) + list(' ' * 4)   # добавляем 4 пробела, чтобы общее число элементов в строке было 9
            random.shuffle(nums)                # перемешываем список для каждого ряда карточки
            cards.append(nums)

        self.card_user = cards[:3]              # карточка игрока
        self.card_comp = cards[3:]              # карточка компьютера

    def get_card(self, card_player):
        print('{:-^22}'.format(self.name))
        for i, y in enumerate(card_player):
            print(' '.join(y))
        print('-' * 22)

    def search(self, card_player, num_cask):    # поиск номера и подсчет очков
        for i, n in enumerate(card_player):
            if str(num_cask) in n:              # проверка есть ли в ряду карточки есть номер бочонка num_cask
                n[n.index(str(num_cask))] = '-'
                self.score += 1
                print(self.score)
                if self.score == 15:
                    print(f'!!! {self.name} выиграла !!!')
                    sys.exit(1)
                return True
        return False


class Player(Lotto):

    def __init__(self, name):
        super().__init__()
        self.name = name


def main_game():
    the_game = Lotto()                              # экземпляр игры
    cask = Cask()
    the_user = Player('Ваша карточка')              # имя игрока
    the_comp = Player('Карточка компьютера')        # имя компьютера

    while True:
        num_cask = next(cask.cask_gen)   # запуск генератора Cask - выбирается номер  бочонка из "мешочка" <class 'int'>
        the_user.get_card(the_game.card_user)       # формирование карточки игрока
        the_comp.get_card(the_game.card_comp)       # формирование карточки игрока

        user_answer = input('Есть такой номер? (y/n):')
        if user_answer == 'y':
            if the_user.search(the_game.card_user, num_cask):
                continue
            else:
                print('Игра закончена')
                sys.exit(1)
        if user_answer == 'n':
            if the_user.search(the_game.card_user, num_cask):
                print('Игра закончена')
                sys.exit(1)
            elif the_comp.search(the_game.card_comp, num_cask):
                continue
        if user_answer != 'n' and user_answer != 'y':
            print('Введите y или n !')
            time.sleep(3)
            continue


main_game()
