class Worker:

    def __init__(self, name='Ducke', surname='Nukem', position='imperator', wage=100, bonus=20):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']


new_master = Position('DOOM', 'ROCK', 'palpatin', 1110, 6666)
print(f'New attributes are: {new_master.name}, {new_master.surname}, {new_master.position}, {new_master._income}')
print(f'Total salary of {new_master.get_full_name()} is {new_master.get_full_salary()}')