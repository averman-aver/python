file = open('3_task_file.txt')
lines = file.readlines()
m = 0.0
for line in lines:
    word = float(line.split()[1])
    m = m + word
    if word < 20000.00:
        print(line)
print('Средняя зарплата: ', m)
