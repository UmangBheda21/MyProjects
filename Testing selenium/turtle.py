import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
my_turtle = turtle.Turtle()
my_turtle.pencolor("black")
my_turtle.pensize(3)

# Draw a square
for _ in range(4):
    my_turtle.forward(100)  # Move forward by 100 units
    my_turtle.right(90)     # Turn right by 90 degrees

# Close the window when clicked
screen.exitonclick()
