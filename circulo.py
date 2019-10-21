
import turtle               #llamamos a tortuga
wn = turtle.Screen()        #creamos una ventana
isa = turtle.Turtle("turtle")       #creamos una tortuga, la asignamos a una variable y le decimos que tome la figura de una tortuga
isa.circle(30)      #crea un circulo
isa.penup()         #no traza el camino de la tortuga puedo usar tambien solo up
isa.goto(-30,30)    # la tortuga se dirige a unas coordenadas    
isa.pendown()       # la tortuga vuelve a dibujar
isa.left(90)        #gira la tortuga en sentido horario
isa.forward(90)
isa.circle(25,180)
isa.right(0)
isa.forward(90)
isa.penup()
isa.goto(-140,30)
isa.pendown()
isa.circle(30)