import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.setup(width=500, height=450)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter Color ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtles = []


def color_assign():
    for colour in colors:
        if colour == user_bet:
            colors.remove(colour)


def instances(color, y_axiss):
    tom = Turtle(shape="turtle")
    tom.color(color)
    tom.penup()
    tom.goto(-230, y_axiss)
    turtles.append(tom)


color_assign()
y_axis = 120
turtles.append(tim)
tim.shape("turtle")
tim.color(user_bet)
tim.penup()
tim.goto(-230.00, y_axis)


for color in colors:
    y_axis = y_axis - 40
    instances(color, y_axis)


is_race_on = False

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've WON! The {winning_color} turtle is the winner")
            else:
                print(f"You've LOSE! The {winning_color} turtle is the winner")
            # exit()
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)




#
# y_axis = y_axis - 40
# tim = Turtle()
# tim.shape("turtle")
# tim.color(colors[0])
# tim.penup()
# tim.goto(-230.00, y_axis)
#
# y_axis = y_axis - 40
# tim = Turtle()
# tim.shape("turtle")
# tim.color(colors[1])
# tim.penup()
# tim.goto(-230.00, y_axis)
#
# y_axis = y_axis - 40
# tim.shape("turtle")
# tim.color(colors[2])
# tim.penup()
# tim.goto(-230.00, y_axis)
#
# y_axis = y_axis - 40
# tim = Turtle()
# tim.shape("turtle")
# tim.color(colors[3])
# tim.penup()
# tim.goto(-230.00, y_axis)
#
# y_axis = y_axis - 40
# tim = Turtle()
# tim.shape("turtle")
# tim.color(colors[4])
# tim.penup()
# tim.goto(-230.00, y_axis)

screen.exitonclick()
