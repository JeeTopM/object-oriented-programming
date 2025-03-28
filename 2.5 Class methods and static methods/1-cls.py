class Library:
    @classmethod
    def book(cls, x, y):
        cls.x = x
        cls.y = y
        print(cls.x * cls.y)
Library.book(5, 20)