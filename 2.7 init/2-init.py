"""
Предыстория:

Вася улучшает свою соцсеть Person. При создании странички, пользователь указывает обязательные данные, 
    и нажимая на кнопку "создать", создаётся страница с данными пользователя.
"""
class Person:
    def __init__(self, name, age, study, work):
        self.name = name
        self.age = age
        self.study = study
        self.work = work

id_1 = Person('Vasya', 22, 'college', 'developer')
print(id_1.__dict__)