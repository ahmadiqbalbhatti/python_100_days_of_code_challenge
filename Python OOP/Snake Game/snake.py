from turtle import Turtle
from scoreboard import ScoreBoard

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.x_coordinate = 0.00
        self.all_segments = []
        self.is_game_on = True
        self.creat_snake()
        self.head = self.all_segments[0]

    def creat_snake(self):
        for _ in range(0, 3):
            segments = Turtle(shape="square")
            segments.color("white")
            segments.penup()
            segments.goto(self.x_coordinate, 0.00)
            self.x_coordinate = self.x_coordinate - 20
            self.all_segments.append(segments)

    #
    # def move(self):
    #     for segment in self.all_segments:
    #         segment.penup()
    #         if segment.xcor() > 300:
    #             segment.goto(-300.00, 0.00)
    #         segment.forward(MOVE_DISTANCE)

    def move(self):
        for seg_number in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg_number - 1].xcor()
            new_y = self.all_segments[seg_number - 1].ycor()
            self.all_segments[seg_number].goto(x=new_x, y=new_y)

        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.all_segments.append(new_segment)

    def extent_segment(self):
        self.add_segment(self.all_segments[-1].position())

    def reset_game(self):
        for seg in self.all_segments:
            seg.goto(1000, 1000)
        self.all_segments.clear()
        self.creat_snake()
        self.head =  self.all_segments[0]
    # def detect_head_collision(self):
    #     # snake_without_head = snake.all_segments[1:len(snake.all_segments)]
    #     for segment in self.all_segments[1:]:
    #         # if segment == snake.head:
    #         #     pass
    #         if self.head.distance(segment) < 10:
    #

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

