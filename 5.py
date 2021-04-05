# Предполагаем что список отсортирован и не нуждается в сортировка. Иначе сначала можно выполнить сортировку списка.
my_list = [7, 5, 3, 3, 2]
#vvod = int(input('Введите число:'))
while True:
    try:
        vvod = int(input('Введите число: '))
        break
    except ValueError:
        print('Введите число, говорю, иначе санитаров вызрвем')
for i in range(len(my_list)):
    if vvod > my_list[i]:
        my_list.insert(i, vvod)
        break
    elif i == len(my_list) - 1:
        my_list.append(vvod)
print (my_list)