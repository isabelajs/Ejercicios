import turtle

def figura (t, sz):     
    """ hace un cuadrado"""            
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor("lightblue")

isa = turtle.Turtle("turtle")
isa.pensize(2)
figura(isa,20)

tamaño = 20
for i in ["blue", "red","green", "purple", "pink"]: # creo un ciclo para cambiar de color la figura y el angulo
    isa.color(i)
    tamaño += 20
    figura(isa,tamaño)
    isa.right(72)
    