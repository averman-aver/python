#5
er = 'qwertuiey'
print(type(er.find('e')))
print('индекс', er.find('e'))



def sum_string_func():
    his_string = input('Введите строку чисел, разделенных пробелом (клавиша "q" - стоп-символ): ')
    marker_q = his_string.find('q')  # маркер наличия стоп-символа, равен -1, если символа нет

    his_string = his_string[:his_string.find('q')]  # получение среза строки до стоп-символа

    if his_string[-1] == ' ':         # проверка нет ли пробела в конце строки
        his_string = his_string[:-1]  # и его удаление
    his_list = his_string.split(' ')  # преобразование строки с пробелами в список чисел

    sum_his_string = 0
    for v in his_list:
        sum_his_string = sum_his_string + int(v)  # вычисление суммы чисел из списка
    return (sum_his_string, marker_q)

my_sum = 0
z = sum_string_func()
while z[1] == -1:
    my_sum = my_sum + z[0]
    print('Промежуточная сумма', my_sum)
    z = sum_string_func()
my_sum = my_sum + z[0]
print('Сумма чисел до введения стоп-символа q:', my_sum)
print('The End')