import turtle

star = turtle.Turtle()

star.color("red", "yellow")

star.begin_fill()
for i in range(25):
    star.forward(100)
    star.left(140)

star.end_fill()

turtle.done()

