prirost = int(input('Введите полученную выручку: '))
rashod = int (input('Введите издержки: '))
if prirost < rashod:
    print(f'Издержки больше прибыли, придется голодать. У нас убытков {rashod - prirost} дэнге')
elif prirost == rashod:
    print('В ноль сработали. Выручка равна издержкам. Один фиг голодать')
elif prirost > rashod:
    profit = prirost - rashod
    print(f'Хорошо поработали. Прибыль составила {profit} дэнге')
    rent = profit / prirost
    print(f'Рентабельность составила {rent:.2f} или {rent*100:.0f}%')
    sotrud = int(input('Какова численность сотрудников в фирме???: '))
    print(f'Каждый сотрудник принес фирме {profit / sotrud}')
