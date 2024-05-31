import random
from punkty import Point


class Apple(Point):
    def __init__(self, max_x :int, max_y :int):
        super().__init__(0, 0, 'A')
        self.__max_x = max_x
        self.__max_y = max_y
        self.x = random.randint(0 ,self.__max_x)
        self.y = random.randint(0 ,self.__max_y)


    def set_new_place(self, points):
        is_ok = True
        while is_ok:
            is_ok = False
            self.x = random.randint(0,self.__max_x)
            self.y = random.randint(0,self.__max_y)
            for point in points:
                if self.x == point.x and self.y == point.y:
                    is_ok = False

