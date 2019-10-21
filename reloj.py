import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")

isa = turtle.Turtle("turtle")

for i in range(12):
    isa.goto(0,0)
    isa.left(30)
    isa.up()
    isa.forward(80)
    isa.down()
    isa.forward(20)
    isa.up()
    isa.forward(40)
    isa.stamp()
    isa.forward(-140)


