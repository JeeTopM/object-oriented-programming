"""
Задание:

Создайте класс BeautyTransform и два метода: __init__, transformer.
Метод __init__ имеет два параметра: height, weight и создаёт два атрибута 
    height, weight со значениями параметров height, weight соответственно. 
    Также, __init__ создаёт атрибут result = "Божественная красота".
Метод transformer(self) содержит внутри конструкцию try-except-else-finally:
- В блоке try cоздаётся атрибут new_body равный делению self.height / self.weight
- Блок except проверяет код на разные ошибки, поэтому применяется except Exception. 
    Если ошибка обнаружится, атрибут result получает новое значение: "Индюк на три дня"
- Блок else выводит сообщение на экран: Проверка прошла! В print() также используется end=' '
- Блок finally выводит сообщение на экран: Результат: result. Где result - это значение атрибута result.
Часть кода уже написана, вам нужно лишь сделать задание выше.
Sample Input:
Sample Output:
Проверка прошла! Результат: Божественная красота
Проверка прошла! Результат: Божественная красота
Результат: Индюк на три дня
"""
# Создайте класс и методы


# Код ниже пожалуйста не меняйте, ради Васи
nastya = BeautyTransform(100, 50)
lena = BeautyTransform(50, 90)
vasya = BeautyTransform(172, "Индюк")

nastya.transformer()
lena.transformer()
vasya.transformer()