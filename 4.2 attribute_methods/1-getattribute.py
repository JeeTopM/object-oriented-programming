# Допишите код так, чтобы на экран выводились слова, указанные в Sample Output. Для этого создайте метод __getattribute__ .

class User:
    def __init__(self, name):
        self.name = name    

    # создайте метод __getattribute__
    def __getattribute__(self, name):
        return object.__getattribute__(self, name) + 'man'

user1 = User("Super")
user2 = User("Bat")
user3 = User("Spider")

print(user1.name, user2.name, user3.name, sep='\n')