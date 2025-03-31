"""
Вася понял работу __dict__ и решил использовать её в своей соцсети Person. 
В этот раз он придумал быстрый способ, как сразу добавить группу людей в друзья, для этого он использует __dict__ и обычный словарь. 
У Васи есть словарь людей, которых он планирует добавить, помогите ему осуществить этот быстрый способ.
 
"""

class Person:
    pass

vasya = Person()

# напишите ваш код:
data = {'id_1':'Masha', 'id_2':'Tom Cruise', 'id_3':'Nicole Kidman', 'id_4':'Brad Pitt', 'id_5':'Tom Hanks', 'id_6':'Johnny Depp'}
vasya.__dict__.update(data)

# код ниже пожалуйста не удаляйте
for key, value in vasya.__dict__.items():
    print(key, value)