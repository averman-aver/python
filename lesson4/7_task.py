def factorial(n):
    x = 1
    factorial = []
    for i in range(1, n+1):
        x = i * x
        i += 1
        factorial.append(x)
    return factorial



def fact(n):
    for m in factorial(n):
        yield m

#print(factorial(7))

for el in fact(5):
    print(el)