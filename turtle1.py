import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,400)
shape = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides
for i in range(num_sides):
    shape.forward(side_length)
    shape.right(angle)
turtle.done()