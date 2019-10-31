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
tess.color("pink")  # la ultima es la verdad las otras son estampas verifica al darle otro color
wn.exitonclick()
