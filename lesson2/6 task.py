#6

good = {}
good_param = ()
goods = []
a = {}
list_analitics = []
result = {}

max_quantity = int(input('Количество товаров в структуре данных:'))
for i in range(1, max_quantity + 1):
    name = input('Наименование товара :')
    price = int(input('Цена товара :'))
    quantity = int(input('Количество товара :'))
    unit = input('Единица измерения :')
    good = {'name': name, 'price': price, 'quantity': quantity, 'unit': unit}
    #print(good)
    good_param = (i, good)
    goods.append(good_param)
print(goods)

analitics = input('Введите параметр для анализа (name, price, quantity, unit) :')

for good in goods:
    print(good[1])
    a = good[1]
    list_analitics.append(a[analitics])

result[analitics] = list_analitics
print(result)