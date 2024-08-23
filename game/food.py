from turtle import Turtle
from turtle import Screen
import random

screen = Screen()

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        max_x = int(screen.window_width() / 2) - 20
        max_y = int(screen.window_height() / 2) - 20
        random_x = random.randint(-max_x, max_x)
        random_y = random.randint(-max_y, max_y)
        self.goto(random_x, random_y)
        
    def reset(self):
        self.refresh()