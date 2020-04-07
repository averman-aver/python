my_list = [3, 5, 2, 78, 4, 90]
#print(my_list[my_list.index(78)-1])
my_sort_list = (x for x in my_list if x > my_list[my_list.index(x)-1])

for i in my_sort_list:
    print(i)