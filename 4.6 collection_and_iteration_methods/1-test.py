"""
Задание:
Часть кода уже написана.
Создайте подходящие методы, чтобы результат стал верным.
Внимательно присмотритесь к уже написанному коду и результату, и проявите изобретательность.
Sample Input:
Sample Output:
['Nokia', 'Xiaomi', 'Huawei', 'LG', 'HONOR']
HONOR
"""
class MyPhone:
    def __init__(self):
        self.phone = ['Nokia', 'Iphone', 'Samsung', 'Huawei', 'LG']

    def __str__(self):
        return str(self.phone)

    # напишите ваши методы


# код ниже не меняйте, но присмотритесь
my_phone = MyPhone()

my_phone[1] = 'Xiaomi'
del my_phone[2]
my_phone.kruchu_verchu('HONOR')

print(my_phone)
print(my_phone[4])