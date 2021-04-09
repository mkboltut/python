def sum_max_func(a, b, c):
    list_max = [a, b, c]
    mini = list_max.pop(list_max.index(min(list_max)))
    sum_max = sum(list_max)
    print (f'Найдено минимальное число: {mini}')
    return sum_max


a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))
z = sum_max_func(a, b, c)
print(f'Сумма максимальных двух чисел равна: {z}')
