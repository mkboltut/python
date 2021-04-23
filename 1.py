import time


class TrafficLight:
    __color = 'red'
    _i = 3
    count_change = 0
    def running(self):
        TrafficLight.count_change += 1
        print('Светофор работает')
        print(f'Идет цикл смены цветов №{TrafficLight.count_change}')

        self.__color = 'Красный'
        print(f'\033[38mЗагорелся цвет:\033[33m {self.__color}')
        time.sleep(7)

        self.__color = 'Жёлтый'
        print(f'\033[38mВоспылал:\033[32m {self.__color}')
        time.sleep(2)

        self.__color = 'Зелёный'
        print(f'\033[38mВот тебе и море разверзлось:\033[31m {self.__color}')
        time.sleep(5)




traff_light = TrafficLight()
while True:
    i = input(f'\033[38mПереходим через дорогу? (y or n): ')
    if i == 'y':
        traff_light.running()
    elif i == 'n':
        print(f'\033[38mБудь внимателен, твой мозг может ввести тебя в заблуждение, например с цветами')
        break
    else:
        print(f'\033[38mВведи n или y')
