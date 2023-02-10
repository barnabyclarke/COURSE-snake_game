from turtle import Turtle
import random
RANDOM_POSITION = range(-280, 280, 20)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.choice(RANDOM_POSITION)
        random_y = random.choice(RANDOM_POSITION)
        self.goto(random_x, random_y)
