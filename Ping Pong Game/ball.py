from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.move_speed *= 0.9
        self.x_move *= -1

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()
