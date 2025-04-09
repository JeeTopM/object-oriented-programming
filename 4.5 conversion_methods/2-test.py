"""
Задание:

Создайте класс, нужные методы, атрибуты и экземпляр. 
    Затем, выведите на экран информацию об экземпляре для программистов. 
    Пример вывода написан ниже (Sample Output). 
    Используйте информацию из примера, чтобы написать код:
    Класс: Car, Атрибуты экземпляра: {'model': 'toyota corolla', 'color': 'black', 'year': 2023}
"""
# v.3
class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
    def __repr__(self):
        return f"Класс: {self.__class__.__name__}, Атрибуты экземпляра: {self.__dict__}"
    

car = Car('toyota corolla', 'black', 2023)
print(car)

# v.1
"""
class Car:
    model = 'toyota corolla'
    color = 'black'
    year = 2023

    def __repr__(self):
        return f"Класс: Car, Атрибуты экземпляра: {{'model': '{self.model}', 'color': {self.color}, 'year': {self.year}}}"

car = Car()
print(car)
"""

# v.2
"""
class Car:
    def __init__(self, model=None, color=None, year=None):
        self.model = model
        self.color = color
        self.year = year
    def __repr__(self):
        return f"Класс: Car, Атрибуты экземпляра: {{'model': '{self.model}', 'color': '{self.color}', 'year': {self.year}}}"

car = Car()
car.__dict__ = {'model': 'toyota corolla', 'color': 'black', 'year': 2023}
print(car)
"""