import turtle as t
import random

squirtle = t.Turtle()
t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    generated_colour = (r, g, b)
    return generated_colour


squirtle.speed("fastest")
def draw_spirograph(size_of_graph):
    for i in range(int(360/size_of_graph)):
        squirtle.color(random_colour())
        squirtle.circle(100)
        squirtle.setheading(squirtle.heading()+size_of_graph)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
