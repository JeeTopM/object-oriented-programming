"""
Предыстория:

У Васи день рождения, и три друга (Masha, Nikita, Lena) придут с подарком. Вася любит красный цвет.
Маша подарила: pen, цвета: red
Никита подарил: t-shirt, цвета: red
Лена подарила: ball, цвета: red
"""
class BirthDay:
    def __init__(self, present, color='red'):
        self.present = present
        self.color = color

masha = BirthDay('pen')
nikita = BirthDay('t-shirt')
lena = BirthDay('ball')

print(f'Маша подарила: {masha.present}, цвета: {masha.color}')
print(f'Никита подарил: {nikita.present}, цвета: {nikita.color}')
print(f'Лена подарила: {lena.present}, цвета: {lena.color}')