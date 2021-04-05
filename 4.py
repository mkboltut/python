vvod = input('Введите текст: ')
sp = vvod.split()
for i, v in enumerate(sp, start=1):
    print(f'№{i} {v[:10:]}')
