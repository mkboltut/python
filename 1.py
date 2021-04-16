my_file = open('text1.txt', 'a+')
while True:
    string = input('Введите строку: ')
    my_file.write(string + '\n')
    if len(string) == 0:
        break
