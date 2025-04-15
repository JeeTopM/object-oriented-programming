"""
Задание:
Создайте класс BeautyTransform и два метода: __init__() и transformer().
Метод __init__() имеет два параметра: height и weight=0, и создаёт два атрибута height и weight с этими же значениями. 
    Параметр weight=0 - это параметр по умолчанию, равный нулю.
Метод transformer(self) содержит внутри конструкцию try-except.
В блоке try происходит две операции:
- Создаётся атрибут new_body равный делению self.height / self.weight
- С помощью print() выводится на экран сообщение: Успешная трансформация ​​​​​​
Блок except проверяет код на ошибку ZeroDivisionError, и если она обнаружится, выводит на экран текст:
Лицо как в картине Крик, Эдварда Мунка
Часть кода уже написана, вам нужно лишь сделать то, что написано выше.  
Sample Input:
Sample Output:
Успешная трансформация
Успешная трансформация
Лицо как в картине Крик, Эдварда Мунка
"""
# Создайте класс и методы
class BeautyTransform:
    def __init__(self,height, weight=0):
        self.height = height
        self.weight = weight
    
    def transformer(self):
        try:
            self.new_body = self.height / self.weight
            print('Успешная трансформация')
        except ZeroDivisionError:
            print('Лицо как в картине Крик, Эдварда Мунка')

# Код ниже пожалуйста не меняйте
vasya = BeautyTransform(172, 70)
nastya = BeautyTransform(100, 50)
lena = BeautyTransform(50)

vasya.transformer()
nastya.transformer()
lena.transformer()