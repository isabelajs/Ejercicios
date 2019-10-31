def exponente (a,b):
    x = 1
    b = abs(b) # utilizo valor absoluto para que funcione con negativos
    for i in range(b):
        x = x*a
    return x

base = 2
Eleva = 2
y = exponente(base,Eleva)
print(y)