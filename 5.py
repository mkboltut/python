class Stationary:
    def __init__(self, title='Название'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):

    def draw(self):
        self.title = 'Ручка'
        print(f'\033[38mВот {self.title} тут линия \033[34m синяя')


class Pencil(Stationary):

    def draw(self):
        self.title = 'Карандаш'
        print(f'\033[38mВот {self.title} тут линия \033[32m зелёная')


class Handle(Stationary):

    def draw(self):
        self.title = 'Маркер'
        print(f'\033[38mВот {self.title} тут линия\033[1;30;47m жирная и черная \033[0;0m')


pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()