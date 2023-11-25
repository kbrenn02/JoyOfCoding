# draw shapes using turtle
# Kevin Brennan

import turtle
turtle.shape("turtle")

#shape functions
def square(len):
    for i in range(4):
        turtle.forward(len)
        turtle.right(90)

def triangle(side):
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)

def house(size):
    square(size)
    triangle(size)

def rectangle(wid, len):
    for i in range(2):
        turtle.forward(wid)
        turtle.right(90)
        turtle.forward(len)
        turtle.right(90)

def octagon(side):
    for i in range(8):
        turtle.forward(side)
        turtle.left(45)

def stop(side):
    octagon(side)
    turtle.forward((3/8)*side)
    rectangle((1/5)*side, 2*side)

# #draw house
turtle.speed(1)
turtle.color("lime green")
# house(50)
#
# turtle.penup()
# turtle.forward(100)
# turtle.pendown()
# turtle.color("skyblue")
#
# house(100)


#draw stop sign
# rectangle(10, 90)
turtle.penup()
turtle.back(100)
turtle.pendown()

stop(50)

turtle.penup()
turtle.forward(100)
turtle.pendown()

stop(75)

turtle.penup()
turtle.back(100)
turtle.pendown()

stop(100)

turtle.Screen().exitonclick()

