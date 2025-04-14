"""
Задание:
Часть кода уже написана
Объявите нужные методы, чтобы класс выполнял роль декоратора. 
    Функция с декоратором должна возвращать число в три раза больше, чем число, которое возвращает функция. 
    Например, функция принимает 5 страницы и возвращает 5 страницы, а декоратор делает так, что функция вернёт 15.
В функции ничего не меняйте, вам нужно лишь объявить нужные методы в классе.
Sample Input:
Sample Output:
15
"""
class ReadingAccelerator:
    # ваши методы
    def __init__(self, number):
        self.number = number

    def __call__(self, *args, **kwargs):
        res = self.number(*args, **kwargs)
        return res * 3

@ReadingAccelerator
def masha_reading(page_number):
    return page_number

print(masha_reading(5))