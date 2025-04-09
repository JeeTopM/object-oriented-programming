# 80 -1.0 10 100 -30 10

class Number:
    # Объявите здесь все необходимые методы для операций
    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        return self.number + other
    def __truediv__(self, other):
        return self.number / other
    def __mul__(self, other):
        return self.number * other
    def __pow__(self, power):
        return self.number ** power
    def __sub__(self, other):
        return self.number - other
    def __abs__(self):
        return abs(self.number)


# код ниже не меняйте ради вселенной
num1 = Number(-10)
result1 = num1 + 90
result2 = num1 / 10
result3 = num1 * -1
result4 = num1 ** 2
result5 = num1 - 20
result6 = abs(num1)
print(result1, result2, result3, result4, result5, result6)
