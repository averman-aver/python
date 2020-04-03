#6

def int_func(text):
    return (text.capitalize())

not_my_str = 'ert rtt rr p0p'
print('Исходная строка: ', not_my_str)
not_my_list = (not_my_str.split(' '))  # разборка исходной строки в список чепез пробел в качестве разделителя

not_my_list_cap = []
for i in not_my_list:
    not_my_list_cap.append(int_func(i))  # применение функции к элементам разобранного списка и формирование нового списка

not_my_str_cap = ''
for j in not_my_list_cap:
    not_my_str_cap = not_my_str_cap + ' ' + j  # склейка получившегося преобразованного списка в строку

print(not_my_str_cap)