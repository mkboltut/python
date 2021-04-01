time = int(input('Введите время в секундах: '))
hour = time // 3600
minute = (time // 60) % 60
sec = time % 60
print (f'время - {hour:02}:{minute:02}:{sec:02}')
