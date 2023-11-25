# turtle program
# Kevin Brennan

import turtle
turtle.shape("turtle")

#square function
def square(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

#draw square
turtle.speed(1)
turtle.color("lime green")
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
square(50, 60)

turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.color("skyblue")
square(50, 75)

turtle.Screen().exitonclick()