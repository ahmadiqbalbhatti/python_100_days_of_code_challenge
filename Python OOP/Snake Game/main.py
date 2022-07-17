import turtle
from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
count = 0

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while snake.is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect the collision by food
    if snake.head.distance(food) < 25:
        food.food_position()
        snake.extent_segment()
        score.score_calculation()

    position = 290

    if snake.head.xcor() > position or snake.head.xcor() < -position or snake.head.ycor() > position or snake.head.ycor() < -position:
        snake.game_over()

# x_coordinate = 0.00
# all_segments = []
#
#
# for _ in range(0, 5):
#     segments = Turtle(shape="square")
#     segments.color("white")
#     segments.penup()
#     segments.goto(x_coordinate, 0.00)
#     x_coordinate = x_coordinate - 20
#     all_segments.append(segments)
#
#
# is_game_on = True
#
# # while is_game_on:
# #     screen.update()
# #     time.sleep(0.1)
# #
# #     for segment_number in range(2, 0, -1):
# #         all_segments[segment_number].goto()
#
# while is_game_on:
#     screen.update()
#     time.sleep(0.5)
#     for segment in all_segments:
#         segment.penup()
#         if segment.xcor() > 300:
#             segment.goto(-300.00, 0.00)
#         segment.forward(20)

# segment_1 = Turtle(shape="square")
# segment_1.color("white")
#
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(-20, 0.0)
#
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(-40, 0.0)

screen.exitonclick()
