"""
Предыстория:
Вася создал волшебное устройство, которое позволяет менять баланс банковского счёта любого человека, с помощью заклинания happy_balance. 
    Вася щедрый малый, и решил пополнить счёт Машеньки. 
    Но в какой-то момент Вася увлёкся и не заметил, как случайно обнулил её счёт. 
    Из-за чего Машенька обиделась на Васю и спрятала активатор телепорта под подушку.
Задание:
Часть кода уже написана
Создайте с помощью геттера, сеттера и делиттера, возможность взаимодействовать с атрибутом __balance.
Геттер возвращает значение баланса.
Сеттер устанавливает новый баланс.
Делиттер не удаляет баланс, но меняет его на число 0.
Посмотрите на код проверки, и подумайте как назвать ваши методы, чтобы всё сработало правильно.
Вам нужно лишь объявить сеттер, геттер и делиттер, всё остальное уже готово.
Sample Input:
Sample Output:
500
1000
0
"""
class MagicBank:
    def __init__(self, account, balance):
        self.__account = account
        self.__balance = balance

    # ваши методы
    @property
    def happy_balance(self):
        return self.__balance
        
    @happy_balance.setter
    def happy_balance(self, value):
        self.__balance = value

    @happy_balance.deleter
    def happy_balance(self):
        self.__balance = 0

# Код проверки пожалуйста не удаляйте

id_1 = MagicBank('Машенька', 500)
print(id_1.happy_balance)

id_1.happy_balance = 1000
print(id_1.happy_balance)

del id_1.happy_balance
print(id_1.happy_balance)