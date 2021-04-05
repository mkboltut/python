while True:
    try:
        MonNum = int(input('Введите номер месяца: '))
        if MonNum not in range(1, 13):
            print('Введите корректный номер месяца')
        else:
            break
    except ValueError:
        print('Число месяца, а не непонятный набор символов')
month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
         'Декабрь']
sezon = ['Зима', 'Весна', 'Лето', 'Осень']
if MonNum in range(3, 6):
    print (sezon[1])
elif MonNum in range(6, 9):
    print (sezon[2])
elif MonNum in range(9, 12):
    print(sezon[3])
else:
    print(sezon[0])
print('Месяц ' + month[MonNum-1])
print('-----------------------------со словарем---------------------')
DicSezon = dict(Январь='Зима', Февраль='Зима', Март='Весна', Апрель='Весна', Май='Весна', Июнь='Лето', Июль='Лето',
                Август='Лето', Сентябрь='Осень', Октябрь='Осень', Ноябрь='Осень', Декабрь='Зима')
print('Месяц ' + month[MonNum-1])
print('Время года ' + DicSezon.get(month[MonNum-1]))