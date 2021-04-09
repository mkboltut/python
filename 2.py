def man_func(name, surname, age, state, email, phone):
    print(f'ФСБ изучило материалы и тепер точно знает о вас зовут {name} {surname}, полных лет {age} '
          f'Живет {state}, электронная почта {email} номер телефона {phone}')


name = input('Введите имя ')
sur = input('Фамилия ')
age = input('Полных лет ')
state = input('Город ')
email = input('Мыло ')
ph = input('Телефон ')
print(man_func(name=name, surname=sur, age=age, phone=ph,email=email, state=state))