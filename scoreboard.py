from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("pixel", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("pixel", 60, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("pixel", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("pixel", 60, "normal"))

    def l_point(self):
        # self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        # self.clear()
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("pixel", 60, "normal"))
