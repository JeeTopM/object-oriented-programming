"""
Вася научился с помощью __dict__ быстро добавлять группы людей в своей соцсети Person. 
Теперь ему нужно быстрым способом увидеть список всех друзей, нажав на одну кнопку. Пока он думает использовать цикл и __dict__. 

"""

class Person:
    pass

person_1 = Person()
person_1.__dict__ = {'name': 'Vasya', 'age': '20', 'work': 'driver'}

# ваш код ниже:
for key, value in person_1.__dict__.items():
    print(value)

"""
for value in person_1.__dict__:
    print(person_1.__dict__[value])
"""