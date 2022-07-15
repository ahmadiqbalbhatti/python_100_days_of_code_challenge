from turtle import Screen, Turtle

timmy = Turtle()
print(timmy)

my_screen = Screen()

print(my_screen.window_height())
print(my_screen.window_width())

timmy.shape("turtle")


timmy.color("coral")
timmy.forward(100)
my_screen.exitonclick()
