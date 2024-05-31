from Point import Point




class Snake():
    def __init__(self, max_x, max_y, start_x, start_y):
        self.__max_x = max_x
        self.__max_y = max_y
        self.body = [Point(start_x, start_y, '@')]
        self.direction = Point(1, 0, '')
        self.speed = 0.5

    def move(self):
        #porosz calym wezem
        for i in range(len(self.body)-1, 0,-1):
            self.body[i].x =self.body[i-1].x
            self.body[i].y =self.body[i-1].y


        self.body[0].x +=self.direction.x
        self.body[0].y +=self.direction.y

        if self.body[0].x > self.__max_x:
            self.body[0].x =0
        if self.body[0].y > self.__max_y:
            self.body[0].y =0

        if self.body[0].y < 0:
            self.body[0].y =self.__max_y

        if self.body[0].x < 0:
            self.body[0].x = self.__max_x

    def add_body(self):
        self.body.append(Point(self.body[0].x, self.body[0].y, 'x'))




