"""
Задача:

Часть кода уже написана.
Переменная input_word принимает разные строки.
Напишите ваш код в методе __str__, чтобы команда print(person) выводила сообщение "Да здравствует input_word!". 
    Естественно input_word здесь переменная, и будет принимать разные слова. 
"""
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Да здравствует {self.name}!"

# Код ниже пожалуйста не меняйте:        
input_word = input()
person = Person(input_word)
print(person)