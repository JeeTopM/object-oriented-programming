"""
Вступление:
Машенька побывала уже на нескольких планетах (Сатурн, Юпитер, Земля, Марс). 
    Но она сильно желает побывать ещё на двух планетах: Плутон и Венера. 
    Выведите на экран все планеты на которых Машенька уже побывала и планирует побывать, согласно примеру ответа.
Задание:
Часть кода уже написана, используйте уже написанные данные и дополните код.
Используйте в обязательной форме, методы __init__, __enter__ и __exit__.
Планета Венера требовательная, и её можно указывать только в методе __exit__.
Выведите все результаты согласно примеру ниже.
Sample Input:
Sample Output:
Сатурн
Юпитер
Земля
Марс
Плутон
Венера
"""
planetes = ['Сатурн', 'Юпитер', 'Земля', 'Марс']

class StarTravel:
    def __init__(self, other):
        # допишите код
        

    def __enter__(self):
        # допишите код

    def __exit__(self, exc_type, exc_value, traceback):
        # допишите код


# код ниже пожалуйста не меняйте  
with StarTravel('Плутон') as word:
    for i in word:
        print(i)