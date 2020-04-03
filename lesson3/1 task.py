#1

def division():
    x = int(input('Введите x :'))
    y = int(input('Введите y :'))
    try:
        return round(x / y, 3)
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')

print(division())