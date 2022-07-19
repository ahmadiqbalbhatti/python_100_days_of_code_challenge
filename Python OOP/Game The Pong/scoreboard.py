from turtle import Turtle

FONT = ("Courier", 30, "bold")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(None)
        self.penup()
        self.color("white")
        self.score_l = 0
        self.score_r = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-50, 250)
        self.write(self.score_l, font=FONT, align=ALIGNMENT)
        self.goto(50, 250)
        self.write(self.score_r, font=FONT, align=ALIGNMENT)

    def point_l(self):
        self.score_l += 1
        self.update_score()

    def point_r(self):
        self.score_r += 1
        self.update_score()
