"""
Создайте класс NewJournal.
Объявите два метода: set_attr() и check_money().
Метод set_attr():
- Имеет 4 параметра: papa, mama, deda, baba. Это значит set_attr(self, papa, mama...и т.д.).
- Создаёт атрибуты papa, mama, deda, baba, а значения этих атрибутов будут равны параметрам papa, mama, deda, baba, соответственно.
- Создаёт атрибут count_money равный сумме этих четырёх атрибутов: papa, mama, deda, baba.
Метод check_money():
- Проверяет, если атрибут count_money меньше 80, то выводит на экран: Денег не хватает
- Иначе выводит на экран: Ура, денег хватает!
Создайте экземпляр masha.
Вызовите метод set_attr() через экземпляр masha. 
В аргументах укажите 10, 20, 30, 40 - это наши значения для атрибутов: papa, mama, deda, baba.
Вызовите метод check_money()
Не забывайте про self и скобки при вызове методов.

Ура, денег хватает!
"""
class NewJournal:
    def set_attr(self, papa, mama, deda, baba):
        self.papa = papa
        self.mama = mama
        self.deda = deda
        self.baba = baba
        self.count_money = papa + mama + deda + baba
    def check_money(self):
        print('Ура, денег хватает!' if self.count_money >= 80 else 'Денег не хватает')
masha = NewJournal()
masha.set_attr(10, 20, 30, 40)
masha.check_money()