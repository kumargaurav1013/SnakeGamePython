from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            t1 = Turtle(shape="square")
            t1.color("white")
            t1.penup()
            t1.goto(position)
            self.segments.append(t1)


    def increase_snake_length(self):
        t1 = Turtle(shape="square")
        t1.color("white")
        t1.penup()
        self.segments.append(t1)


    def move(self):
        for seg_ind in range(len(self.segments) - 1, 0, -1):
            pos = self.segments[seg_ind - 1].position()
            self.segments[seg_ind].goto(pos)
        self.segments[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
