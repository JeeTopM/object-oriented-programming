'''
Задание:
Создайте класс Bank
Объявите три метода: __init__, print_balance, change_balance
Метод __init__ имеет три параметра:  имя клиента, номер карты и баланс, и создаёт три приватных атрибута. Имена параметрам и атрибутам придумайте сами.
Метод print_balance является обычным методом, и выводит на экран баланс клиента с помощью print().
Метод change_balance имеет параметр (self, money), и изменяет баланс клиента. 
    Если money отрицательное, то баланс уменьшается, если money положительное, то баланс увеличивается. 
    Метод только изменяет атрибут связанный с балансом.
Часть кода уже написана, вам нужно лишь сделать то, что написано выше.
'''
# ваш класс и методы
class Bank:
    def __init__(self, name, number_card, balance):
        self.__name = name
        self.__number_card = number_card
        self.__balance = balance

    def print_balance(self):
        print(self.__balance)

    def change_balance(self, money):
        self.__balance += money

# код ниже пожалуйста не меняйте
id_1 = Bank('Vasya', 12345678, 500)
id_1.change_balance(-500)
id_1.print_balance()