from turtle import Turtle
ALIGNMENT = "center"
FONT1 = ("Courier", 60, "normal")
FONT2 = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align=ALIGNMENT, font=FONT1)
        self.goto(0, 220)
        self.write("::", align=ALIGNMENT, font=FONT1)
        self.goto(100, 220)
        self.write(self.r_score, align=ALIGNMENT, font=FONT1)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 80)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT2)
        self.goto(0, 0)
        if self.l_score > self.r_score:
            self.write(f"Left Player has won", align=ALIGNMENT, font=FONT2)
        else:
            self.write(f"Right Player has won", align=ALIGNMENT, font=FONT2)
