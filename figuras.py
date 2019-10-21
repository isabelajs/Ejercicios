import turtle
wn = turtle.Screen()
wn.bgcolor("lightpink")

isa = turtle.Turtle()

for i in range (3):
    isa.forward(100)
    isa.left(360/3)

wn.exitonclick()