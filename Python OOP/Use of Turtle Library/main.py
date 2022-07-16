import random
import turtle
from turtle import Screen, Turtle as t
#
# # from turtle import *
#
# timmy = t()
# print(timmy)
#
# my_screen = Screen()
#
# print(my_screen.window_height())
# print(my_screen.window_width())
#
# # timmy.shape("turtle")
# #
# # timmy.color("coral")
# # timmy.backward(200)
# # timmy.color("red")
# # timmy.left(135)
# # timmy.backward(200)
# # timmy.right(-135)
# # timmy.backward(200)
#
# # timmy.shape()
# # print(timmy.xcor())
# # timmy.backward(250)
# # timmy.right(90)
# # timmy.backward(250)
# # timmy.right(90)
# # timmy.backward(250)
# # timmy.right(90)
# # timmy.backward(250)
# # timmy.right(90)
#
# # i=3
# # while i<25:
# #     # timmy.color("blue")
# #     # timmy.backward(50)
# #     # timmy.right(11.25)
# #     # timmy.color("red")
# #     timmy.right(45)
# #     timmy.pendown()
# #     timmy.forward(25)
# #     timmy.penup()
# #     timmy.forward(20)
# #
# #     i = i+1
#
# color = ['red', 'blue', 'orange', 'grey', 'purple', 'red', 'blue', 'orange', 'grey', 'purple', 'red', 'blue', 'orange',
#          'grey', 'purple', ]
#
# # def draw_shape(num_sides):
# #     angle = 360 / num_sides
# #     for _ in range(num_sides):
# #         timmy.forward(75)
# #         timmy.right(angle)
# #
# #
# # for shape_side_n in range(3, 12):
# #     timmy.color(color[shape_side_n])
# #     draw_shape(shape_side_n)
#
# direction = [0, 90, 180, 270, 360, -270, -180, -90]
#
# turtle.colormode(255)
#
#
# from random import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


print(random_color())
#
#
# #
# #
# # timmy.pensize(10)
# # timmy.speed('fastest')
# # for _ in range(0, 500):
# #     timmy.forward(25)
# #     timmy.color(random_color())
# #     timmy.setheading(random.choice(direction))
#
#
# timmy.speed('fastest')
# for _ in range(int(360/5)):
#     timmy.color(random_color())
#     timmy.circle(50)
#     current_heading = timmy.heading()
#     timmy.setheading(current_heading + 5)
#     timmy.circle(50)
#
# my_screen.exitonclick()
