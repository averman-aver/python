#4

def my_funct(x, y):
    i = 0
    comp = 1
    while i < abs(y):
        comp = comp * x
        print(comp)
        i = i + 1
    result = 1 / comp
    print(result)
    print(x ** y)  # применение встроенной функция

my_funct(9, -5)