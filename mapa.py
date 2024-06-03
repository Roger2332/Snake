class Map:
    def __init__(self, size_x, size_y, empty_char=' '):
        self.__size_x = size_x
        self.__size_y = size_y
        self.__empty_char = empty_char
        self.__map = []
        for y in range(self.__size_y):
            self.__map.append([])
            for x in range(self.__size_x):
                self.__map[y].append(self.__empty_char)

    def clean(self):
        for y in range(self.__size_y):
            for x in range(self.__size_x):
                self.__map[y][x] = self.__empty_char

    def print(self):
        for y in range(self.__size_y):
            for x in range(self.__size_x):
                print(self.__map[y][x], end='')
            print()

    def set_point(self, point):
        self.__map[point.y][point.x] = point.char











