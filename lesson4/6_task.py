
from itertools import count, cycle

mylist1 = []
for i in count(10):
    if i > 20:
        break
    mylist1.append(i)
    print(i, end=' ')
print('\n')
print(mylist1)

j = 0
mylist2 = ['er', 5, 67]
for x in cycle(mylist2):

    if j > 10:
        break
    j += 1

    print(x, end=' ')
print('\n')

