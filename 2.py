lines = 0
null_lines = 0
for line in open('text1.txt', 'r'):
    if len(line) == 1:
        null_lines += 1
    else:
        lines += 1
        words = len(line.split())
        print(f'В строке {lines + null_lines} всего слов {words}')

print("Всего со словами строк: ", lines)
print("Всего пустых строк: ", null_lines)