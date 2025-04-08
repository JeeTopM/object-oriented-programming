"""
Задание:

Создайте класс Number и объявите метод __init__. Метод имеет параметры (self, number), и создаёт атрибут number со значением number.
Объявите метод __add__ (self, other) который позволяет складывать экземпляры с экземплярами, а также экземпляры с целыми числами. 
    Учтите, что при сложении, будет складываться атрибут "number + number" двух экземпляров, и "number + целое число".
Создайте два экземпляра num1 и num2, с атрибутом number равным 100 и 200 соответственно.
Выведите на экран результаты трёх сложений, каждый на отдельной строке:
num1 + num2
num1 + 300
num2 + 300
Результат сложения будет число, смотрите пример ответа ниже.

Sample Output:
300
400
500
"""

class Number:
    def __init__(self, number):
        self.number = number
    
    def __add__(self, other):
        if isinstance(other, Number):
            return self.number + other.number
        elif isinstance(other, int):
            return self.number + other

num1 = Number(100)
num2 = Number(200)

res1 = num1 + num2
res2 = num1 + 300
res3 = num2 + 300

print(res1, res2, res3, sep='\n')