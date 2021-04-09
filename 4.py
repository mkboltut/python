# При округлении число до 4 знаков после запятой стоит выбирать небольшие числа, иначе получим 0, что логично
def expo_func(x, y):
    z = x ** y
    return z


def expo_func2(x, y):
    z = 1/(x ** abs(y))
    return z


def expo_func3(x, y):
    g = x
    for i in range(1, abs(y)):
        g *= x
    z = 1 / g
    return z


while True:
    try:
        x = float(input('Введите действительное число x: '))
        y = int(input('Введите число отрицательной степени: '))
        if y < 0 < x:
            break
        else:
            print('Степень должна быть отрицательной а возводимое число положительным')
    except ValueError:
        print('Нужно число')
print(f'{expo_func(x, y):.4}')
print(f'{expo_func2(x, y):.4}')
print(f'{expo_func3(x, y):.4}')