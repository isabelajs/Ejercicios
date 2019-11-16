alicia = open("alice.txt", "a+")
alicia.write ("I was angry with my friend;\nI told my wrath, my wrath did end.\nI was angry with my foe:\nI told it not, my wrath did grow.") 
alicia.seek(0)
contenido = alicia.readlines()
alicia.close()
print(contenido)



