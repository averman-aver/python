#2
members = []
how_many = int(input("Количество ?"))
i = how_many

while i > 0:
    name = input("Ввдите имя :")
    members.append(name)
    i-=1
print(members)

j = 0
while j < len(members):
    fiction = members[j]
    if (j+1) == len(members):
        break
    members[j] = members[j+1]
    members[j+1] = fiction
    j = j+2
print(members)