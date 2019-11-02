import turtle
import math
import random

fred = turtle.Turtle()

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)

fred.up()  # dibujo el circulo con radio 0,0
fred.goto(0,-1)
fred.down()
fred.circle(1)
fred.up()
turtle.speed(10)
numdarts = 100
adentro = 0
for i in range(numdarts):
    fred.home()  #vuelve al punto 0,0
    randx = random.uniform(-1.0,1.0)  # toma un rango para hacer la seleccion tomando decimales
    randy = random.uniform(-1.0,1.0)
    distancia = fred.distance(randx,randy)
    fred.goto(randx,randy)
    if  distancia <= 1: # toma la distancia desde el punto en que me encuento es decir 0,0 hasta donde quiera
        fred.dot(10, "blue")
        adentro += 1
    else:
        fred.dot(10, "red")

pi = (adentro / numdarts)*4
print(pi)  
   
       
    
   
    
  
    

 
wn.exitonclick()