from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
POSITION = (-230, 250)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(POSITION)
        self.write(f"Level:{self.level}", align=ALIGNMENT, font=FONT)

    def inc_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
