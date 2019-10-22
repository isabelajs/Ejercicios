import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setworldcoordinates(0,-2,360,2)

fred = turtle.Turtle()

#levanto para que no se pinte
fred.up()
#la muevo mas adelante
fred.goto(0,0)
#vuelvo a bajar el puntero
fred.down()


#ejecuto varias veces el loop
for veces in range(0,5):
    
    #el rango devuelve el valor entre (0,360] osea sin tomar el 360 asi que debo ponerlo entre (0,361] para que tome el 360
    for angle in range(0,361):
        
        y = math.sin(math.radians(angle))
        fred.goto(angle+(veces*360),y)
        
        #solo para ver la posicion de x
        print(fred.pos())
        
        #reposicionar las coordenadas de la pantalla en x = la posicion del angle osea x - 100 para verlo desde atras + (veces * 360) para
        #saber cuantos x he recorrido, lo mismo para x2 
        wn.setworldcoordinates(angle-100+(veces*360),-2,360+angle-100+(veces*360),2)

wn.exitonclick() 
