file = open('2_task_file.txt')
lines = file.readlines()

print('Строк: ', len(lines))

i = 1
for line in lines:
    words = line.split()
    print('Слов в строке', i, ':', len(words))
    i += 1
