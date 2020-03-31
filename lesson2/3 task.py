#3
#list
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
winter = [1, 2, 12]
mounth = int(input("Введите номер месяца: "))

if mounth in spring:
    print("весна")
elif mounth in summer:
    print("лето")
elif mounth in autumn:
    print("осень")
elif mounth in winter:
    print("зима")

else:
    print("Неверный ввод месяца")

#dict
year = {'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11], 'winter': [1, 2, 12]}
mounth = int(input("Введите номер месяца: "))
if mounth <=0 or mounth > 12:
    print("Неверный ввод месяца")

for key, val in year.items():
    if mounth in val:
        print(key)