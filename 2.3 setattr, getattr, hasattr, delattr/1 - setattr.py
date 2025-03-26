class Person:                       # Создайте пустой класс Person (внутри будет pass).
    pass                            # pass
id_1 = Person()                     # Создайте экземпляр id_1 класса Person.
setattr(id_1, "name", "Vasya")      # Создайте в экземпляре атрибут name и присвойте ему значение "Vasya"
setattr(id_1, "name", "Masha")      # Измените на "Masha"
print(id_1.name)                    # Вывод на экран