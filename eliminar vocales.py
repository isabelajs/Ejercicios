s = "holamiimir"
vocales = "aeiouAEIOU"
sinvocales = ""
# for cadaCar in s:
#     if cadaCar not in vocales:
#         sinvocales = sinvocales + cadaCar        #quita las vocales
# print(sinvocales)
for cadaCar in s:
    sinvocales = cadaCar.upper()+ sinvocales        # pone en mayuscula y lo agrega al reves
print(sinvocales)