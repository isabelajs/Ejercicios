import turtle
clr_fondo = input("ingrese un color")

wn = turtle.Screen()
wn.bgcolor(clr_fondo)        #cambiar el color del fonodo de la ventana

tess = turtle.Turtle()
color_tess = input("ingrese un color") #pregunta el color que queremos
tess.color(color_tess)              #cambia el color de la tortuga por el que ingresamos
tess.pensize(10)                 #cambia el tamaño de la tortuga


tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                #cuando damos click se sale de la ventana
