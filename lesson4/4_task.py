
import collections
my_list = [1, 1, 3, 4, 5, 2, 78, 4, 4,  90]

gen = (x for x, count in collections.Counter(my_list).items() if count == 1)  # решение с collections подсмотрено в инете

my_sort_list = []
for el in gen:
    my_sort_list.append(el)

print(my_sort_list)

#print([x for x, count in collections.Counter(my_list).items() if count == 1])