from turtle import Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Game The Pong")
screen.tracer(0)
screen.listen()

# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.speed("fastest")
# paddle.goto(x=350, y=0)


# def go_up():
#     new_y = paddle.ycor()
#     new_y = new_y + 20
#     paddle.goto(paddle.xcor(), new_y)
#
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)


paddle_r = Paddle(375)
paddle_l = Paddle(-375)

ball = Ball()

score = ScoreBoard()
# score_right = ScoreBoard()

screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        score.point_r()

    if ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        score.point_l()

    if ball.xcor() > 380:
        ball.reset_position()
        score.point_l()

    if ball.xcor() < -380:
        ball.reset_position()
        score.point_r()

screen.exitonclick()
