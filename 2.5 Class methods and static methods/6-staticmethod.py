"""
Вася использует программирование в повседневной жизни. 
В этот раз он пишет программу, показывающую истёк ли срок годности у товара или нет. 
Он указывает сегодняшнюю дату и дату окончания товара и получает ответ. 
Для этого он нестерпимо решил использовать статический метод.
"""
from datetime import datetime

class Product:
    @staticmethod
    def check_date(today, expiry):
        start = datetime.strptime(today, "%Y-%m-%d")
        finish = datetime.strptime(expiry, "%Y-%m-%d")
        if finish > start:
            print('Срок годности в порядке')
        else:
            print('Срок годности истёк')

today_date = "2024-01-12"
expiry_date1 = "2024-01-31"
expiry_date2 = "2024-01-1"
expiry_date3 = "2024-01-12"

Product.check_date(today_date, expiry_date1)
Product.check_date(today_date, expiry_date2)
Product.check_date(today_date, expiry_date3)