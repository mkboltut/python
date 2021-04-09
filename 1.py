def del_func(a, b):
    try:
        z = a / b
    except ZeroDivisionError:
        z = 'На ноль пока не научился делить'
    return z


while True:
    try:
        print(del_func(int(input('Введите делимое: ')), int(input('Введите делитель: '))))
    except ValueError:
        print('Не надо в меня пихать всякую гадость')
    else:
        break
