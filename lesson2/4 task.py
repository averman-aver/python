#4
some_string = input("Введите любые слова, разделяя их пробелами :")
print(some_string)
some_list_new = some_string.split(" ")
i = 0
while i < len(some_list_new):
    print("№", (i+1), some_list_new[i][:9])
    i+=1