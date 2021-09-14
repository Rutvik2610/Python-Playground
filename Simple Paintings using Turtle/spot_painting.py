import turtle as t
import random

squirtle = t.Turtle()
t.colormode(255)
squirtle.speed("fastest")
squirtle.penup()
squirtle.hideturtle()
squirtle.setx(-200)
squirtle.sety(-200)
squirtle.pendown()

colour_list = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (224, 141, 62), (197, 144, 171), (143, 180, 206),
               (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132),
               (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (58, 47, 41),
               (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145), (182, 194, 199),
               (215, 176, 187), (223, 178, 168), (54, 45, 52)]


def draw_spot_painting():
    for i in range(10):
        for j in range(10):
            new_colour = random.choice(colour_list)
            squirtle.color(new_colour)
            squirtle.dot(20)
            squirtle.penup()
            squirtle.forward(40)
            squirtle.pendown()
        squirtle.penup()
        squirtle.setx(squirtle.xcor() - 400)
        squirtle.sety(squirtle.ycor() + 40)


draw_spot_painting()
screen = t.Screen()
screen.exitonclick()
