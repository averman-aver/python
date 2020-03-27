first_day_run = int(input('Дистанция  пробежки в первый день, км: '))
results = int(input('Желаемый результат пробежки, км:'))
day_number = 1
day_run = first_day_run
while day_run < results:
    day_run = first_day_run * 1.1 ** (day_number - 1)
    #day_run = day_run * 1.1
    print('День ', day_number, ' - ', day_run, ' км')
    day_number = day_number +1
print('День достижения результата - ', day_number-1)