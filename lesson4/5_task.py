
from functools import reduce

my_list = []

my_gen = (x for x in range(100, 1001) if x%2 == 00)

for el in my_gen:
    my_list.append(el)

product = (reduce(lambda x, y: x * y, my_list))
print(my_list)
print(product)