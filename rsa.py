'''
FIAP
Defesa Cibernética
Development & Coding for Security

Prof. Ms. Fábio H. Cabrini
Atividade: Check Point 4
Alunos
Victor Dias Gonçalves - RM88582
Filipe Grahl - RM86663
'''

# Modules:
import random

# criar 2 numero primos
def gerarNP():
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
    79, 83, 89, 97, 101, 103]
    return random.choice(primos)

# Totiente de euler
def phi(p, q): 
    return (p - 1) * (q - 1)

# Gerar E
def gerarE(n):
    def mdc(n1,n2):
        rest = 1
        while(n2 != 0):
            rest = n1%n2
            n1 = n2
            n2 = rest
        return n1

    while True:
        e = random.randrange(2,n) 
        if(mdc(n,e) == 1):
            return e

# Calculo do modulo
def mod(a,b): 
    if(a<b):
        return a
    else:
        c=a%b
        return c

# Criptografa o texto
def criptografia(text,e,n):
    tam = len(text)
    i = 0
    lista = []
    while(i < tam):
        letra = text[i]
        k = ord(letra)
        k = k**e
        d = mod(k,n)
        lista.append(d)
        i += 1
    return lista
    
# Decriptografia 
def decriptografa(cifra,n,d):
    lista = []
    i = 0
    tamanho = len(cifra)
    while i < tamanho:
        result = cifra[i]**d
        texto = mod(result,n)
        letra = chr(texto)
        lista.append(letra)
        i += 1
    return lista

def priKey(phi,e):
    d = 0
    while(mod(d*e,phi)!=1):
        d += 1
    return d

if __name__=='__main__':
    text = input("Insert message: ")
    p = gerarNP()
    q = gerarNP()
    n = p*q
    on = phi(p, q)
    e = gerarE(n)
    d = 1 / e
    pubKey = (n, e)
        
    print('Your public key:', pubKey)
    textoCript = criptografia(text,e,n)
    print('Your encrypted message:', textoCript)
    d = priKey(on, e)
    print('Your private key is:', d)
    textoDecript = decriptografa(textoCript,n,d)
    print('your original message:', textoDecript)