# ваш код:
class Counter:
    count = 0
    @classmethod
    def add_count(cls, add=1):
        cls.count += add
    @classmethod
    def set_zero(cls):
        cls.count = 0


# код ниже пожалуйста не удаляйте
Counter.add_count()
Counter.set_zero()
Counter.add_count(110)
Counter.add_count()
print(Counter.count)