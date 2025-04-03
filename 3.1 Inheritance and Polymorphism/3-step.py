"""
Предыстория:

Вася программирует и составляет родословную на компьютере. Кондратий Палыч - это дедушка Маши, а Вася - это отец Маши. 
    Но что-то пошло не так и получилось, что Маша - это отец, а Вася - это дед. Исправьте пожалуйста код, чтобы было всё верно.
"""
class Kondraty_Palich:
    status = 'Деда'

class Vasya(Kondraty_Palich):
    status = 'Отец'

class Masha(Vasya):
    status = 'Дочь'

masha = Masha()
vasya = Vasya()

print(masha.status, vasya.status, sep='\n')