import turtle


def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    count = 0
    # print(n)   # imprime n el número al que queremos evaluar
    while n != 1:
        if n % 2 == 0:        # n dividido en 2 es igual a 0
            n = n // 2
        else:                 # n is impar (odd)
            n = n * 3 + 1
        count +=1             # cuenta el número de ciclos
    # print(count)
    return count




wn = turtle.Screen()
wn.bgcolor("light blue")
wn.setworldcoordinates(0,0.5,110,800)

isa = turtle.Turtle("turtle")
isa.color("red")

for start in range (1,6):
    
    isa.left(90)
    isa.forward(seq3np1(start)*100)
    isa.write(int(seq3np1(start)*100))
    isa.right(90)
    isa.forward(20)
    isa.right(90)
    isa.forward(seq3np1(start)*100)
    isa.left(90)


wn.exitonclick()