
    # count = 0
    # word = {}
    # for i in palabra:
    #     if i == "e":
    #         count = count +1
    #         word [i] =count
    #     if i == "s":
    #         count = count +1
    #         word [i] =count
    # return word



a = list("see")
word = {}

for letra in a:
    contar = 0
    for x in range(len(a)):
        if letra == a[x]:
            x = letra
            contar += 1
            word[letra] = contar
print(word)

def countAll (palabra):
    newList = list(palabra)
    diccionario = {}

    for letra in newList:
        contar = 0
        for posicion in range(len(newList)):
            if letra == newList[posicion]:
                clave = letra
                contar += 1
                diccionario[clave] = contar
    print(diccionario)

countAll("moon")