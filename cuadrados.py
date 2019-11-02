import turtle

def drawsquare(t,sz):
    for i in range (4):
        t.forward(sz)
        t.left(90)

wn= turtle.Screen()
wn.bgcolor("lightblue")

isa = turtle.Turtle("turtle")
isa.color("pink")
isa.pensize(3)

tamaño = 20
for i in range(2):
    drawsquare(isa,tamaño)
    isa.goto(0-10,0-10)
    tamaño += 20

wn.exitonclick()
