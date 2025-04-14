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
    def __getitem__(self, item):
        return self.phone[item]

    def __setitem__(self, index, value):
        self.phone[index] = value
    
    def __delitem__(self, index):    
        del self.phone[index]

    def kruchu_verchu(self, value):
        self.phone.append(value)

    def __str__(self):
        return str(self.phone)

# код ниже не меняйте, но присмотритесь
my_phone = MyPhone()

my_phone[1] = 'Xiaomi'
del my_phone[2]
my_phone.kruchu_verchu('HONOR')

print(my_phone)
print(my_phone[4])