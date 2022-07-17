from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(None)
        self.penup()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.goto(-50, 275)
        self.write(f"Score: {self.score}", font=("Arial", 16, "normal"))

    def score_calculation(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"Score: {self.score}", font=("Arial", 16, "normal"))
        # self.write()
