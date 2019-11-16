
palabra = input("ingresa una palabra ")
alfabeto= "abcdefghijklmnopqrstuvwxyz"
contar_diccionario = {}

for caracter in palabra:
    if caracter in alfabeto:
        if caracter in contar_diccionario:
            contar_diccionario[caracter] += 1
        else:
            contar_diccionario[caracter] = 1
            
print(contar_diccionario)
 

