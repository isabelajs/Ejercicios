x = input("Enter a sentence")

x = x.lower()   # convierte todo en minuscula

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_count = {} # diccionario vacio
for char in x:
    if char in alphabet: # ignore any punctuation, numbers, etc
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1

keys = letter_count.keys()
for char in sorted(keys):
    print(char, letter_count[char])