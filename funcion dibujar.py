import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")  #darle forma a la tortuga
tess.up()

for size in range(10):    
    tess.forward(50) 
    tess.stamp()               #marque con la tortuga
    tess.forward(-50)   
    tess.right(40)           
tess.color("pink")
wn.exitonclick()
