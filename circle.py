# Takes a radius (int) as commandline parameter. Draws something resembling a circle with the given radius using the turtle module.
# The turtle should alternatively move forward or turn left/right so that it stays at about radius pixels from the center of the screen.
# Experiment with varying turning angles and movement distances.
# Do not use the circle() function - that would be too easy.


import sys
import turtle
import math


# draw circle with turtle
def draw_circle(radius):
    # add a bit of color and basic settings
    turtle.bgcolor('yellow')
    turtle.color('red')
    turtle.pencolor('blue')
    turtle.turtlesize(2)
    turtle.speed(5)

    # reposition the turtle - the center position is not the best for a huge circle
    turtle.penup()
    turtle.setposition(0, radius)

    # draw the circle
    turtle.pendown()
    move_turtle(radius)


# move the turtle on a circle with given radius
# found calculation for this on this page: https://stackoverflow.com/questions/64647096/how-to-draw-a-circle-using-turtle-in-python
def move_turtle(radius):
    for i in range(360):
        turtle.forward((2 * math.pi * radius) / 360)
        turtle.right(1.0)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        integer = int(sys.argv[1])
    else:
        print("you forgot to enter an integer on the command line - please enter a number")
        integer = int(sys.stdin.readline())
    draw_circle(integer)
