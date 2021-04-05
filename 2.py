a = input('введите набор символов: ')
d = list(a)
for i in range(0, len(d), 2):
    if i == len(d) - 1:
        break
    a = d[i]
    b = d[i+1]
    d[i] = b
    d[i+1] = a
print(d)

