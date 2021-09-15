from turtle import Turtle
MOVE_DISTANCE = 30


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(pos)

    def move_up(self):
        if self.ycor() < 240:
            new_ycor = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_ycor)

    def move_down(self):
        if self.ycor() > -240:
            new_ycor = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_ycor)
