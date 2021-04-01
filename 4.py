pislo = int(input('Введите число: '))
i = 0
while pislo > 0:
    n = pislo % 10
    if i < n:
        i = n
    else:
        pislo //= 10
print (i)