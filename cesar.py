import string
import sys
file = open('arquivo.txt' , 'r')
rotation = int(input("Input the key: "))
message = str(file.read().lower())
alfabet = list(string.ascii_lowercase)
result = ''
for character in message:
    if character in alfabet:
        position = alfabet.index(character)
        position = (position - rotation) % 26
        result = result + alfabet[position]
    print (result)
file.close()
