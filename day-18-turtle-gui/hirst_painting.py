import colorgram
import turtle
import random

colors = colorgram.extract('image.jpg', 10)

colors = list(colors)


def random_color():
    return random.choice(colors).rgb


turtle.colormode(255)


t = turtle.Turtle()
t.width(20)
t.teleport(-290.0, -200.0)
screen = turtle.Screen()
screen.cv._rootwindow.attributes("-topmost", True)
for y in range(-150, 301, 50):
    for i in range(20):
        t.color(random_color())
        if i % 2 == 0:
            t.penup()
            t.forward(50)
        else:
            t.pd()
            t.forward(1)
    t.teleport(-290, y)

screen.exitonclick()
