from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"{self.score_l}", align="center", font=("Arial", 20, "normal"))
        self.goto(100, 250)
        self.write(f"{self.score_r}", align="center", font=("Arial", 20, "normal"))

    def left_user_score(self):
        self.score_l += 1
        self.score_update()
    def right_user_score(self):
        self.score_r += 1
        self.score_update()