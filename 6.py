while True:
    try:
        step = int(input('Введите количество товаров: '))
        if step < 0:
            print('Не должно быть отрицательного количества товаров')
        else:
            break
    except ValueError:
        print('Это интересно сколько?')
my_list = []
# Валидацию значений словаря делать не стал((( времени не хватило, на работе регресс полным ходом
for i in range(step):
    name = input('Имя товара: ')
    cost = input('Цена товара: ')
    quan = input('Количество товара: ')
    ed = input('Единица измерения товара: ')
    dic = {'Name': name, 'Cost': cost, 'quantity': quan, 'unit': ed}

    cargo = (i + 1, dic)
    my_list.append(cargo)
# print(my_list)
stats = {}
# Не придумал как короче сделать
for i in my_list:
    if stats.get('Name') is None:
        stats['Name'] = [i[1].get('Name')]
    else:
        stats.get('Name').append(i[1].get('Name'))

    if stats.get('Cost') is None:
        stats['Cost'] = [i[1].get('Cost')]
    else:
        stats.get('Cost').append(i[1].get('Cost'))

    if stats.get('quantity') is None:
        stats['quantity'] = [i[1].get('quantity')]
    else:
        stats.get('quantity').append(i[1].get('quantity'))

    if stats.get('unit') is None:
        stats['unit'] = [i[1].get('unit')]
    else:
        stats.get('unit').append(i[1].get('unit'))
print (stats)
