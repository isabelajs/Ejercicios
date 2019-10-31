import turtle
clr_fondo = input("ingrese un color para el fondo ") # pregunta que color queremos para el fondo

wn = turtle.Screen()          #asigna una variable para la ventana
wn.bgcolor(clr_fondo)        #cambiar el color del fondo de la ventana

tess = turtle.Turtle()         # invoca la tortuga por defecto es una flecha
color_tess = input("ingrese un color para la tortuga ") #pregunta el color que queremos en la tortuga
tess.color(color_tess)              #cambia el color de la tortuga por el que ingresamos
tess.pensize(10)                 #cambia el tamaño de la tortuga


tess.forward(50)               #camina 50 pasos
tess.left(120)                 # gira 120 en contra del sentido horario
tess.forward(50)

wn.exitonclick()                #cuando damos click se sale de la ventana
