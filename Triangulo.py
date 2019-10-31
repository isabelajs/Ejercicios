import turtle
wn = turtle.Screen()
wn.bgcolor("lightpink")

isa = turtle.Turtle()

for i in range (3):
    isa.forward(100)       #camina 100 pasos
    isa.left(360/3)         # divide 360 grados en 3 para obtener 3 grados o puntos

wn.exitonclick()