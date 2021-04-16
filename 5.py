import random

with open('text5.txt', 'w+') as file_wr:
    line = ' '.join(([str(random.randint(1, 255)) for i in range(25)]))
    file_wr.writelines(line)
    my_numb = line.split()
with open('text5.txt', 'r', encoding="utf-8") as file_open:
    summ_file = sum(list(map(int, file_open.read().split())))
print(summ_file)