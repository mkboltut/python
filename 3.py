with open('text3.txt', 'r', encoding="utf-8") as my_file:
    salary = []
    minimal = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
           minimal.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20.000 {" ,".join(minimal)}, средний оклад {sum(map(float, salary)) / len(salary):.2f}')