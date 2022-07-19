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
        # self.high_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.goto(0, 270)
        self.update_score(f'Score: {self.score}')

    def update_score(self, string):
        self.clear()
        self.write(f'{string}, High Score: {self.high_score}', font=FONT, align=ALIGNMENT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score(f'Score: {self.score}')

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.update_score("GAME OVER")

    def score_calculation(self):
        self.score += 1
        self.update_score(f'Score: {self.score}')
