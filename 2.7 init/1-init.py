"""
Предыстория:

Вася тренируется в программировании GPS навигации. 
Он учится ставить точку на 2D карте используя создание экземпляров с координатами x и y. 

"""
class Coordinate:
    def __init__(self, x, y):
        self.coordinate_x = x
        self.coordinate_y = y

coord = Coordinate(100, 200)
print(coord.coordinate_x, coord.coordinate_y)