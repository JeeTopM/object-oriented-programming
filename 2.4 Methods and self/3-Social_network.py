'''
Часть кода уже написана.
Создайте метод print_number_of_messages(). Метод выводит на экран значение атрибута message_counter. 
У каждого экземпляра свой атрибут message_counter, поэтому используйте self.
В самом конце, выведите на экран количество сообщений у экземпляра id_1 и id_2. 
Каждый ответ на отдельной строке (см. пример ответа ниже).
'''

class Person:
    message_counter = 0
    # объявите ваш метод
    def print_number_of_messages(self):
        print(self.message_counter)

id_1 = Person()
id_2 = Person()

id_1.message_counter = 5
id_2.message_counter = 10

# ваш код вызова метода:
id_1.print_number_of_messages()
id_2.print_number_of_messages()