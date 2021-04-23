class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} погнал.'

    def stop(self):
        return f'\n{self.name} встал.'

    def turn(self, direction):
        return f'\n{self.name} повернул, надеюсь туда, {direction}'

    def show_speed(self):
        return f'\nСкорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВы слишком низко летите! Скорость равна {self.speed}'
        else:
            return f'Скорость {self.name} как у черепахи'


class SportCar(Car):
    def show_speed(self):
        return 'Ты че тут забыл, бегом отбивать контрабанду у глоксов'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВы слишком низко летите! Скорость равна {self.speed}'
        else:
            return f'Скорость {self.name} как у черепахи'


class PoliceCar(Car):
    def show_speed(self):
        return 'О темнейший, не смеем задерживать!!!!'


town = TownCar('Боливар', 90, 'ржавый', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('на лево'), town.turn('на право'), town.stop())

sport = SportCar('Энтерпрайз', 200, 'зеленый', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('на лево'), sport.stop())

work = WorkCar('Сокол тысячелетия', 140, 'красный', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('на право'), work.stop())

police = PoliceCar('Палачь', 1000000, 'чёрный', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('на право'), police.stop())