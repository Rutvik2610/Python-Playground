import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

blastoise = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(blastoise.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # Detect if turtle reached the finish line
    if blastoise.ycor() > 300:
        blastoise.reset_position()
        score.inc_level()
        car_manager.increase_speed()

    # Detect collision with car
    for car in car_manager.all_cars:
        if blastoise.distance(car) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()
