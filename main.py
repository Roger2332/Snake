from strzalki import GetKey, clear_console, wait
from punkty import Point
from apple import Apple
from  mapa import Map
from waz import Snake

SIZE_X = 10
SIZE_Y = 10



if __name__ == '__main__':
    my_get_key = GetKey()
    my_apple = Apple(SIZE_X -1, SIZE_Y -1)
    my_maps = Map(SIZE_X, SIZE_Y, " ")
    my_snake = Snake(SIZE_X -1, SIZE_Y -1)
    my_secore = 0



    while True:
        clear_console()
        my_maps.clean()

        key = my_get_key()
        # 27 = esc
        # 299 lewo
        # 301 prawo
        # 296 gora
        # 304 dol


        if key == 27:
            break
        if key == 299 and not (my_snake.direction.x == 1 and my_snake.direction.y == 0):
            my_snake.direction.x = -1
            my_snake.direction.y = 0

        if key == 301 and not (my_snake.direction.x == -1 and my_snake.direction.y == 0):
            my_snake.direction.x = 1
            my_snake.direction.y = 0

        if key == 296 and not (my_snake.direction.x == 0 and my_snake.direction.y == 1):
            my_snake.direction.x = 0
            my_snake.direction.y = -1

        if key == 304 and not (my_snake.direction.x == 0 and my_snake.direction.y == -1):
            my_snake.direction.x = 0
            my_snake.direction.y = 1



        my_snake.move()
        game_over = False
        for i in range(1, len(my_snake.body)):
            if my_snake.body[0].x == my_snake.body[i].x and my_snake.body[0].y == my_snake.body[i].y:
                print("Game over")
                game_over = True
        if game_over == True:
            break

        if my_snake.body[0].x== my_apple.x and my_snake.body[0].y== my_apple.y:
            my_snake.add_body()
            my_apple.set_new_place(my_snake.body)
            my_secore +=1

        my_maps.set_point(my_apple)



        if my_snake.speed > 0.1:
            my_snake.speed -=0.01





        for i in range(len(my_snake.body) -1, -1, -1):
            my_maps.set_point(my_snake.body[i])

        #wyswietl mape
        my_maps.print()
        print(f"SECORE: {my_secore}")
        #czekaj
        wait(my_snake.speed)


