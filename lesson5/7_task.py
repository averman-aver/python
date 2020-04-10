import json
profit = {}
a_p = {}
prof = 0
aver_prof = 0  # prof_aver
n = 0
with open('7_task_file.txt', 'r') as f:
    #print(type(f))
    for line in f:
        name, firm, earning, damage = line.split()  # название. форма собственности. выручка. издержки
        #print(line.split())
        profit[name] = int(earning) - int(damage)  # форм. словарь, где ключу "название фирмы присваивается значение прибыли"
        #print('profit', profit)
        if profit[name] >= 0:
            prof = prof + profit[name]  # суммируется положительная прибыль
            n += 1  #накапливание количества фирм с положительной прибылью
    if n != 0:
        aver_prof = round(prof / n, 2)
        print('Средняя прибыль:', aver_prof)
    else:
        print('Нет прибыли')
    a_p = {'average_profit': round(aver_prof)}
    profit.update(a_p)  # дописывает в словарь profit пару "средняя выручка"
    print('Прибыль по компаниям:', profit)

with open('7_task.json', 'w') as f_js:
    json.dump(profit, f_js)
    str_js = json.dumps(profit)
    print('Json-файл: ', str_js)
