import random
x= random.randrange(30,150)
y = random.randrange(30,150)
print(x)
import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")

isa = turtle.Turtle("turtle")
isa.fillcolor("purple") #para rellenar adentro de la tortuga
isa.up()  # levantar y no pintar el trazo de la tortuga
isa.goto(-300,50)
for i in range (100):
    isa.stamp()
    isa.forward(x)

juan= turtle.Turtle("turtle")
juan.fillcolor("green")
juan.up()
juan.goto(-300,-80)
for i in range (100):
    juan.stamp()
    juan.forward(y)


wn.exitonclick()