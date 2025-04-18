"""
Задание:

Создайте класс Number и объявите два метода: __init__ и __pow__
Метод __init__(self, number) создаёт атрибут number со значением number
Метод __pow__(self, power) возвращает результат возведения number в степень power
Создайте экземпляр num, с атрибутом number равным числу 10
Выведите на экран результат возведения экземпляра num в степень 2

Sample Output:
100
"""
class Number:
    def __init__(self, number):
        self.number = number
    def __pow__(self, power):
        if isinstance(self.number, int):
            return self.number ** power

num = Number(10)
print(num**2)