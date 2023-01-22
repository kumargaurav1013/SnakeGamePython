import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        coord_x = random.randint(-270, 270)
        coord_y = random.randint(-270, 270)
        self.goto(coord_x, coord_y)

