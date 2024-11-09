import turtle
spiral = turtle.Screen()
spiral.bgcolor("dark red")
spiral.title("Spiral")
mypen = turtle.Turtle()
size = 0
while True:
    for i in range(5):
        mypen.fd(size+1)
        mypen.left(75)
        size = size - 5
    size = size + 1
turtle.done()