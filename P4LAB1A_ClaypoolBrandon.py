# Brandon Claypool
# CTI 110
# P4LAB1A - Draw square and triangle with loops

import turtle

# setup
win = turtle.Screen()
t = turtle.Turtle()

# set size and color
t.pensize(3)
t.pencolor("blue")
t.shape("turtle")

# draw a square using a for loop
for side in range(4):        # 0,1,2,3  → 4 sides
    t.forward(100)
    t.left(90)

# move over so the triangle doesn’t sit right on the square
t.penup()
t.forward(150)
t.pendown()

# change color so both shapes are visible
t.pencolor("red")

# draw a triangle using a for loop
# triangle turns 360 / 3 = 120 degrees (like turtle4_triangle.py)
for side in range(3):
    t.forward(100)
    t.left(120)

win.mainloop()
