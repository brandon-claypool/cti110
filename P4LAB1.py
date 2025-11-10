# Brandon Claypool
# P4LAB1a
# Draws a square and a triangle using loops
# Uses techniques from:
# - https://opentechschool.github.io/python-beginners/en/simple_drawing.html
# - http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html

import turtle

# --- Pseudocode ---
# 1. Create a window and a turtle
# 2. Define a function to draw any polygon using loops (from ThinkCS example)
# 3. Use the function to draw a square and a triangle
# 4. Move the turtle so both shapes are visible
# 5. Keep the window open

# --- Step 1: Setup ---
win = turtle.Screen()
t = turtle.Turtle()

# --- Step 2: Customize turtle (from OpenTechSchool examples) ---
t.shape("turtle")
t.pensize(4)
t.speed(3)

# --- Step 3: Define polygon drawing function ---
def draw_polygon(turtle_obj, sides, length, color):
    """Draws a regular polygon with a given number of sides and side length"""
    turtle_obj.pencolor(color)
    angle = 360 / sides
    for i in range(sides):
        turtle_obj.forward(length)
        turtle_obj.left(angle)

# --- Step 4: Draw a square ---
draw_polygon(t, 4, 100, "blue")

# --- Step 5: Move turtle to a new location for the triangle ---
t.penup()
t.forward(150)
t.pendown()

# --- Step 6: Draw a triangle ---
draw_polygon(t, 3, 100, "red")

# --- Step 7: Keep window open ---
win.mainloop()
