from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.penup()
        self.sety(270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.points}", align=ALIGNMENT, font=FONT)

    def add_points(self):
        self.points += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
