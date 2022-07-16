import random
import turtle

# import colorgram

from turtle import Screen, Turtle as Tl

# colors = colorgram.extract('spot.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     my_new_color = (r, g, b)
#     rgb_colors.append(my_new_color)

# print(rgb_colors)

tim = Tl()
turtle.colormode(255)
color_list = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50),
              (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132),
              (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177),
              (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185),
              (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]
random_color = random.choice(color_list)
print(random_color)
screen = Screen()

screen.window_width()
screen.window_height()

print(tim.pos())
tim.penup()
tim.goto(-49.99, -49.99)
tim.pendown()
tim.forward(225)
tim.penup()
tim.goto(-49.99, -49.99)
tim.left(90)
tim.pendown()
tim.forward(225)
tim.right(90)
tim.penup()
tim.goto(-39.99, -39.99)
position_y = -39.99
tim.pensize(10)
tim.speed('fast')
tim.shapesize(2)
tim.hideturtle()
for _ in range(0, 10):
    position_y = position_y + 20
    for _ in range(0, 10):
        random_color = random.choice(color_list)
        tim.color(random_color)
        tim.pendown()
        tim.forward(1)
        tim.penup()
        tim.forward(20)
    tim.goto(-39.99, position_y)

screen.exitonclick()
