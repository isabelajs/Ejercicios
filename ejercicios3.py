import turtle

def drawsquare(t,sz):
    for i in range (4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor("light blue")

isa = turtle.Turtle("turtle")
isa.color("pink")
isa.pensize(4)
isa.up()
isa.goto(-100,0)
isa.down()

for i in range(5):
    drawsquare(isa,40)
    isa.up()
    isa.forward(70)
    isa.down()
    