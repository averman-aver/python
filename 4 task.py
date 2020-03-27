number0 = int(input('Введите целое положительное число:'))
max = 0
while number0 > 0:
    dig = (number0%10)
    print (dig)
    number0 = (number0//10)
    if max < dig:
        max = dig
print('Максимальная цифра:', max)