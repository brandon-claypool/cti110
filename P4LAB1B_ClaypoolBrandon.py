# Brandon Claypool
# CTI 110
# P4LAB1B - Draw initials (B C) using turtle graphics


import turtle

# setup
win = turtle.Screen()
t = turtle.Turtle()
t.pensize(5)
t.shape("turtle")
t.speed(3)

# Draw the letter B
t.pencolor("blue")
t.penup()
t.goto(-150, 100)
t.pendown()

# Vertical line
t.setheading(270)
t.forward(120)

# Top to start upper bump
t.penup()
t.goto(-150, 100)
t.pendown()
t.setheading(0)

# Upper horizontal
t.forward(60)

# Upper right curve
t.setheading(315)
t.forward(20)

# Upper middle
t.setheading(270)
t.forward(20)

# Return curve to middle
t.setheading(225)
t.forward(20)
t.setheading(180)
t.forward(60)

# Move to middle line
t.penup()
t.goto(-150, 40)
t.pendown()
t.setheading(0)

# Lower horizontal
t.forward(65)

# Lower right curve
t.setheading(315)
t.forward(22)

# Lower vertical
t.setheading(270)
t.forward(22)

# Lower return curve
t.setheading(225)
t.forward(22)

# Connect back to the vertical line at bottom
t.setheading(180)
t.forward(65)

# Draw the letter C
t.penup()
t.goto(80, 100)
t.pendown()
t.pencolor("green")

# Top of C
t.setheading(180)
t.forward(80)

# Left side down
t.setheading(270)
t.forward(120)

# Bottom of C
t.setheading(0)
t.forward(80)

# Finish
t.penup()
t.hideturtle()
win.mainloop()
