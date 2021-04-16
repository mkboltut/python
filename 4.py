translate = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('text4.txt', 'r', encoding="utf-8") as file_open:
    for i in file_open:
        i = i.split()
        new_file.append(translate[i[0]] + ' - ' + i[2] + '\n')
with open('file_translate.txt', 'w', encoding="utf-8") as file_translate:
    file_translate.writelines(new_file)