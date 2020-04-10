
my_str = '10935468790467'
file = open('5_task_file.txt', 'w' '+')
for i in my_str:
    file.write(' ' + (i))
file.close()

file = open('5_task_file.txt')
lines = file.readline()
sum = 0
for i in lines:
    if i != ' ':
        sum = sum + int(i)
print('Сумма чисел файла: ', sum)
file.close()

