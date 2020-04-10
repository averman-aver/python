file = open('4_task_file.txt')
lines = file.readlines()

for line in lines:
    if 'One' in line:
        a = open('4_1_task_file.txt', 'w')
        a.write(line.replace('One', 'Один'))
    elif 'Two' in line:
        b = open('4_2_task_file.txt', 'w')
        b.write(line.replace('Two', 'Два'))
    elif 'Three' in line:
        c = open('4_3_task_file.txt', 'w')
        c.write(line.replace('Three', 'Три'))
    elif 'Four' in line:
        d = open('4_4_task_file.txt', 'w')
        d.write(line.replace('Four', 'Четыре'))
a.close()
b.close()
c.close()
d.close()
file.close