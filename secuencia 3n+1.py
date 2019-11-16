import turtle


def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    count = 0
    # print(n)   # imprime n el número al que queremos evaluar
    while n != 1:
        if n % 2 == 0:        # n es par (even)
            n = n // 2
        else:                 # n is impar (odd)
            n = n * 3 + 1
        count +=1             # cuenta el número de ciclos
    # print(count)
    return count


wn = turtle.Screen()
wn.bgcolor("light blue")
wn.setworldcoordinates(0,0.5,270,800)

isa = turtle.Turtle("turtle")
isa.color("red")

maxsofar = 0
for start in range (1,50):
    x = int(seq3np1(start))
    isa.left(90)
    isa.forward(x)
    isa.write(x)
    isa.right(90)
    isa.forward(5)
    isa.right(90)
    isa.forward(x)
    isa.left(90)
    if maxsofar < x:
        maxsofar = x

print("es el valor mas grande", maxsofar)

wn.exitonclick()