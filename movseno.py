import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setworldcoordinates(0,-2,360,2) # permite hacer foco de vision en estas coordenadas

fred = turtle.Turtle("turtle")
fred.goto(0,0)      # situa la tortuga en estas coordenas

for angle in range(0,360,30):
    
    y = math.sin(math.radians(angle))
    fred.goto(angle,y)
    fred.stamp()


wn.exitonclick()