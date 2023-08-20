from turtle import Turtle, Screen
from time import sleep


class Lines(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("black")

    def make_single_line(self):
        self.penup()
        self.goto(-300, 0)
        self.pendown()
        for _ in range(100):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)


screen = Screen()


lines = Lines()
lines.make_single_line()



screen.exitonclick()
