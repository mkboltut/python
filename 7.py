import math


def gen_func(num):
    for el in range(1, num + 1):
        yield math.factorial(el)


while True:
    try:
        hop = int(input('Введите число: '))
        break
    except ValueError:
        print('Нужно целое число!!!!')
for i in gen_func(hop):
    print(i)