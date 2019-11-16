palabra = list(input("ingrese una palabra "))
lista_letras = ["-"]*len(palabra)

intentos = len(palabra)+2
while intentos > 0 and   lista_letras != palabra:
    letra = input("ingrese una letra ")
    if letra in palabra:
        posicion = palabra.index(letra)
        lista_letras[posicion] = letra
        intentos -= 1
        print(lista_letras)

    else:
        intentos -= 1
        print("intentalo de nuevo", intentos)
   

