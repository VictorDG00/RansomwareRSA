import string
import sys
file = open('D:\Python\RSA\Teste.txt' , 'r', encoding='utf-8')
rotation = int(input("Input the key: "))
message = str(file.readline().lower())
print(message)
alfabet = list(string.printable)
result = ''

for character in message:
    if character in alfabet:
        position = alfabet.index(character)
        position = (position - rotation) % 100
        result = result + alfabet[position]
    print (result)
file.close()

cript = result

arquivo = open('D:\Python\RSA\cripto.txt', 'w', encoding='utf-8')
arquivo.writelines(result)
arquivo.close

decript = ''
for character in cript:
    if character in alfabet:
        position = alfabet.index(character)
        position = (position + rotation) % 100
        decript = decript + alfabet[position]
    print (decript)