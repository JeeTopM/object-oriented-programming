"""
Задание:

1) Создайте два класса Alfa и Beta (дочерний)
2) В классе Alfa создайте статический метод sum_number используя декоратор @staticmethod. Метод sum_number имеет два параметра (x, y). 
    Помните, что в статических методах не используется self. Сам метод возвращает сумму параметров x, y, используя return
3) В дочернем классе Beta создайте обычный метод result, который имеет 4 параметра (self, x, y, z). Метод:
    * записывает в переменную summa, результат вызова метода sum_number, используя параметры x, y.
        То есть summa = результат вызова sum_number.
    * выводит на экран результат деления переменной summa на параметр z, с помощью print. 
4) Создайте экземпляр test класса Beta
5) Вызовите метод result через экземпляр test, используя аргументы 10, 20, 30. Функцию print() использовать не нужно.
"""
class Alfa:
    @staticmethod
    def sum_number(x, y):
        return x + y
    
class Beta(Alfa):
    def result(self, x, y, z):
        summa = super().sum_number(x, y)
        print(summa / z)

test = Beta()
test.result(10, 20, 30)