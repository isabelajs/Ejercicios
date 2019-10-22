import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setworldcoordinates(2,0,360,2)

fred = turtle.Turtle()

for angle in range(0,360,30):
    y = math.sin(math.radians(angle))
    fred.goto(angle,y)


wn.exitonclick()