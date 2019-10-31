def suma (a):
    if a == 0:
        return 0
    else:
        return(a+suma(a-1))

print(suma(3))