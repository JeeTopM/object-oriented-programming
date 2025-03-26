class Person:                                                   # Создайте класс Person
    setup = ['set_name', 'set_age', 'set_work', 'set_study']    # Объявите внутри класса атрибут setup со значением ...
id_1 = Person()                                                 # Создайте экземпляр id_1 от класса Person
for i in id_1.setup:                                            # С помощью цикла for пройдите по атрибуту setup
    setattr(id_1, i, input())                                   # C помощью setattr(), создайте 4 атрибута с именами взятыми из setup
for value in id_1.setup:
    print(getattr(id_1, value))