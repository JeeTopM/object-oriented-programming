"""
Создайте класс Kitty.
Создайте метод say_hello (не забудьте про self).
Внутри метода создайте print('Hello, Kitty'). Метод выводит на экран строку 'Hello, Kitty'.
Создайте экземпляр cat.
Вызовите метод say_hello через экземпляр cat (не забудьте скобки). Функцию print здесь использовать не нужно.
"""
class Kitty:
    def say_hello(self):
        print('Hello, Kitty')
cat = Kitty()
cat.say_hello()