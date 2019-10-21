import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for i in [0, 1, 2, 3]:      # repite por el número de valores en la lista
    alex.forward(50)
    alex.left(90)

wn.exitonclick()
