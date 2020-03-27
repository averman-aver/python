dohod = float(input('Введите доход Вашей фирмы, млн. руб: '))
izd = float(input('Введите издержки, млн. руб: '))
if dohod > izd:
    rent =100 * (dohod - izd)/dohod
    print(' Вы работаете с прибылью, Рентабельность = ', rent, '%')
    people = int(input('Сколько людей у Вас работает?'))
    rent_for_people = (dohod - izd)/people
    print('Прибыль на одного работающего, тыс. руб - ', (1000 * rent_for_people))
else:
    print('Вы работаете в убыток!')