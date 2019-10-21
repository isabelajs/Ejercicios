import turtle
clr_fondo = input("ingrese un color")

wn = turtle.Screen()
wn.bgcolor(clr_fondo)        # set the window background color

tess = turtle.Turtle()
color_tess = input("ingrese un color")
tess.color(color_tess)              # make tess blue
tess.pensize(3)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas
