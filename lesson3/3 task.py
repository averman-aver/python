#3

def my_func(x, y, z):
    g = [x, y, z]
    g.sort(reverse=True)
    g = g[:len(g)-1]
    print(g)  # проверка
    sum = 0
    for i in g:
        sum = sum + i
    return(sum)

print(my_func(78, 4, 16))