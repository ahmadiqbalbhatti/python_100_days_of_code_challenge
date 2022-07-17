from turtle import Turtle

FONT = ("Courier", 20, "bold")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(None)
        self.penup()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.goto(0, 270)
        self.update_score(f'Score: {self.score}')

    def update_score(self, string):
        self.clear()
        self.write(string, font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.update_score("GAME OVER")

    def score_calculation(self):
        self.score = self.score + 1
        self.update_score(f'Score: {self.score}')
