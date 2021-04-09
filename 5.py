def my_func(vvod):
    vvod = vvod.split()
    if 'q' in vvod:
        vvod.pop(vvod.index('q'))
        result = [int(i) for i in vvod]
        k = sum(result)
        p = 0
    else:
        result = [int(i) for i in vvod]
        k = sum(result)
        p = 1
    return [k, p]


go = 0
while True:
    vvod = input('Введите числа через пробел, для завершения введите q ')
    s = my_func(vvod)
    if s[1] == 0:
        go += s[0]
        print(go)
        break
    else:
        go += s[0]
        print(go)
