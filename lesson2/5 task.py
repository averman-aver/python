#5
my_list = [8, 7, 5, 3, 3, 2]
rating = tuple(my_list)
print('Было :', rating)
user_digit = int(input('Введите число: '))
my_list.append(user_digit)
my_list = sorted(my_list, reverse = True)
print(my_list)
