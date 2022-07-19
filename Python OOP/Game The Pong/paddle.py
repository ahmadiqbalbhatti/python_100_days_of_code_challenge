from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor):
        super(Paddle, self).__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(x=x_cor, y=0)

    def go_up(self):
        new_y = self.ycor()
        new_y = new_y + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

