import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setworldcoordinates(0,-2,360,2)

fred = turtle.Turtle()
fred.goto(0,0)

for angle in range(0,360,30):
    
    y = math.sin(math.radians(angle))
    fred.goto(angle,y)


wn.exitonclick()