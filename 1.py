from sys import argv


def salary_func(hour, cost, prize):
    salary = (hour * cost) + prize
    return salary


try:
    if len(argv) != 4:
        print('Необходимо ввести все три аргумента программы (отработанные часы, стоимость часа, премия) через '
              'пробел, в строгом порядке')
    else:
        print(salary_func(int(argv[1]), int(argv[2]), int(argv[3])))
except ValueError:
    print("Необходимо вводить только числа")
