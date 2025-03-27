"""
Часть кода уже написана.
Создайте экземпляр id_1 класса Person. Не забывайте про скобки Person().
С помощью getattr(), выведите на экран значения трёх атрибутов, используя экземпляр. Каждое значение выводится на отдельной строке, 
начиная с dance, смотрите пример вывода ниже. Не забывайте про кавычки, если используете getattr() вне цикла.
По желанию, используйте цикл for.
"""

list_person = ['hobby', 'work', 'study']

class Person:
    hobby = 'dance'
    work = 'design'
    study = 'college'

# ваш код ниже:
id_1 = Person()

print(getattr(id_1, 'hobby'))
print(getattr(id_1, 'work'))
print(getattr(id_1, 'study'))

for name in list_person:
    print(getattr(id_1, name))
