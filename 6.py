start = int(input('Введите результат первого дня: '))
end = int (input('Введите результат к которому стремимся: '))
day = 1
while start < end:
    start = start + (start * 0.1)
    day += 1
print (day) 

#Вариант два с использованием if и break

start = int(input('Введите результат первого дня: '))
end = int (input('Введите результат к которому стремимся: '))
day = 1
while True:
    start = start + (start * 0.1)
    day += 1
    if start >= end:
        break
print (day) 