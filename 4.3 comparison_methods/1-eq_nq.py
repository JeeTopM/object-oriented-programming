"""
Задание:

Часть кода уже написана, вам нужно лишь объявить метод __eq__
Метод __eq__(self, other) содержит две проверки:
- Если other является экземпляром класса Number, то возвращается результат сравнения (==) атрибутов summa у двух экземпляров класса. 
    То есть self и other здесь являются экземплярами и нужно сравнить атрибуты summa этих экземпляров и вернуть результат.
- Если other является числом (int), то возвращается результат сравнения (==) атрибута summa , с other.
- Для проверки лучше всего использовать isinstance().
"""
class Number:
    def __init__(self, x, y):
        self.summa = x + y

    # объявите метод __eq__
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.summa == other.summa
        elif isinstance(other, int):
            return self.summa == other
        

# код ниже пожалуйста не удаляйте
number_1 = Number(4, 2)
number_2 = Number(5, 5)
print(number_1 == number_2)
print(number_1 == 10)
print(number_2 == 10)