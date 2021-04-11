from itertools import count
from itertools import islice
from itertools import cycle


def my_count (start, stop):
    for el in islice(count(start), stop):
       print(el)
    return ('Расчёт окончен')


print(my_count(int(input('Введите стартовое число: ')), int(input('Введите количество иттераций: '))))
my_list = ['Я', 'НЕ', 'ХОЧУ', 'ХОДИТЬ', 'ПО', 'КРУГУ', '!!!!!!!']
my_print = cycle(my_list)
for i in range(len(my_list)):
    print(next(my_print))
