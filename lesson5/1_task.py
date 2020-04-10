my_file = open('1_task_file.txt', 'w' '+')
my_str = []

while my_str != '':
    my_str = input('Ввод: ')
    my_file.write(my_str + '\n')
print(my_file.readlines(1))
my_file.close()

file = open('1_task_file.txt')
text = file.read()
print(text, end=' ')



