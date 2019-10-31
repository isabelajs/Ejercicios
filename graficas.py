import turtle
wn= turtle.Screen()
wn.bgcolor("lightblue")

isa = turtle.Turtle("turtle")

isa.begin_fill()     # se necesita pintar dentro de una figura, se hace la figura y termina en end
isa.circle(100)
isa.end_fill()
isa.fillcolor("green")


wn.exitonclick()