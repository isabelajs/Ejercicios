import turtle

def drawBar (t, h):
    """Haz que la tortuga t dibuje una barra de altura"""
    t.begin_fill()
    t.left(90)
    t.forward(h)
    t.write(str(h))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(h)        
    t.left(90)
    t.end_fill()
    

xs = [48, 117, 200, 240, 160, 260, 220]  
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)


for a in xs:
    drawBar(tess, a)

wn.exitonclick()





