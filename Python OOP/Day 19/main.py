from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def forwards():
    tim.forward(10)


def backwards():
    tim.backward(10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def clockwise():
    tim.setheading((tim.heading() + 10 ))


def counter_clockwise():
    tim.setheading((tim.heading() - 10))


# def up():
#     tim.setheading(90)
#     tim.forward(20)
#
#
# def down():
#     tim.setheading(270)
#     tim.forward(20)
#
#
# def left():
#     tim.setheading(180)
#     tim.forward(20)
#
#
# def right():
#     tim.setheading(0)
#     tim.forward(20)


screen.listen()
# screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="d", fun=counter_clockwise)
screen.onkey(key="a", fun=clockwise)

# print(screen.listen())
screen.exitonclick()
