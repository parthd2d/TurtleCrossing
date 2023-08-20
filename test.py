from random import randint
from turtle import Screen,Turtle

r=randint(0,255)
g=randint(0,255)
b=randint(0,255)

screen=Screen()
screen.colormode(255)
t=Turtle()
t.color((r,g,b))

screen.exitonclick()


