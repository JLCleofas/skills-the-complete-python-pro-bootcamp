from turtle import Turtle, Screen, colormode, pencolor
import random

timmy_the_turtle = Turtle()

# timmy_the_turtle.speed(1)
# timmy_the_turtle.shape('turtle')

colormode(255)
# # set pen size
# timmy_the_turtle.pensize(10)
timmy_the_turtle.speed(0)

# # create a square
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# # create a dashed line
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# create polygons


def random_rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def random_turtle_color():
    timmy_the_turtle.color(random_rgb_color())


def create_polygon(sides):
    timmy_the_turtle.color(random_rgb_color())
    for _ in range(sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(360 / sides)


def random_walk(steps):
    for _ in range(steps):
        timmy_the_turtle.color(random_rgb_color())
        timmy_the_turtle.setheading(random.choice([90, 180, 270, 360]))
        timmy_the_turtle.forward(25)


screen = Screen()
# set screen to full screen
screen.cv._rootwindow.wm_state("zoomed")
# pop up the screen
screen.cv._rootwindow.attributes("-topmost", True)

# # create polygons from triangle (3 sides) to decagon (10 sides)
# for i in range(3, 11):
#     create_polygon(i)

# random_walk(100)

# # make a star
# while True:
#     random_turtle_color()
#     timmy_the_turtle.forward(200)
#     timmy_the_turtle.left(170)
#     if abs(timmy_the_turtle.pos()) < 1:
#         break


# make a circle
def make_spirograph(increment):
    for _ in range(360 // increment):
        random_turtle_color()
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + increment)


make_spirograph(6)

screen.exitonclick()

# # print a hero name
# import heroes
# print(heroes.gen())
