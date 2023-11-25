# Day 1: Hello World
print("Hello, World!") # first program with JoC
   
# Day 2: Draw a triangle with Turtle
import turtle

distance = 75

#turtle attributes
turtle.shape("turtle")
turtle.color("lime green")

#turtle actions
turtle.forward(distance)
turtle.left(120) #turtle needs to turn to the right by 120 degrees before moving forward again
turtle.forward(distance)
turtle.left(120)
turtle.forward(distance)
turtle.left(120)

i=0
while i < 3:
  turtle.color("red")
  turtle.forward(distance)
  turtle.right(120)
  i+=1
  
# Day 3: for loop
# Day 4: functions
turtle.shape("turtle")
turtle.color("lime green")

def triangle(distance):
  for side in range(3):
    turtle.forward(distance)
    turtle.left(360/3)

def back(len):
  turtle.penup()
  turtle.back(len)
  turtle.pendown()
  
def down(len):
  turtle.penup()
  turtle.right(90)
  turtle.forward(len)
  turtle.left(90)
  turtle.pendown()
  
def square(distance):
  for side in range(4):
    turtle.forward(distance)
    turtle.right(360/4)

triangle(75)
back(25)
triangle(100)
triangle(125)
down(50)
square(75)
square(150)

# Day 5: putting it all together (make it DRY - dont repeat yourself)
turtle.shape("turtle")
turtle.color("lime green")
color_list = ["red", "orange", "yellow", "lime green", "blue", "indigo", "violet", "pink", "black", "brown", "navy", "green"]

def shape(size, sides):
  if sides < 3:
    print("Error: not enough sides. Please select a shape with 3 sides or more.")
    return
  turtle.color(color_list[sides-3])
  for side in range(sides):
    turtle.forward(size)
    turtle.left(360/sides)
  turtle.left(55)

def spiral(len_longest, angle):
  for i in range(len_longest, 10, -10):
    turtle.forward(i)
    turtle.right(angle)


turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
    
spiral(150, 90)
#spiral(150, 60)

#shape(50, 3)
#shape(50, 4)
#shape(50, 5)
#shape(50, 6)
#shape(50, 7)
#shape(50, 8)
#shape(50, 9)
#shape(50, 10)

