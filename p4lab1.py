import turtle
# Eric Corbett
#3/11/2024
#making a program that can draw
# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

# Function to draw a triangle
def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.right(120)

# Set up the turtle
turtle.speed(1) 

# Draw the square
turtle.penup()
turtle.goto(-50, -50)  
turtle.pendown()
draw_square(100)  

# Draw the triangle
turtle.penup()
turtle.goto(0, 0)  
turtle.pendown()
draw_triangle(100)  

# Finish
turtle.done()
