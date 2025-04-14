"""
Задание:
Машенька мечтает слетать в Казахстан к своему другу Васе, помогите ей осуществить мечту. 
    Часть кода уже написана. 
    Вам нужно лишь создать подходящий метод или методы.
Sample Input:
Sample Output:
Ура, Маша летит в Казахстан!
"""
class Country:
    country = ('Russia', 'Ukraine', 'Belarus', 'Kazakhstan', 'Other')

    # создайте метод(ы)
    # Вариант 1
    """def __iter__(self):
        return iter(self.country)"""
    
    # Вариант 2
    def __init__(self):
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.country):
            country = self.country[self.index]
            self.index += 1
            return country
        raise StopIteration

# код ниже, не меняйте, ради Машеньки
country_is = Country()
for i in country_is:
    if i == 'Kazakhstan':
        print(f'Ура, Маша летит в Казахстан!')