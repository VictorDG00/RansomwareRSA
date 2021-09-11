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
import math

# criar 2 numero primos
def gerarNP():
    primos = []
    for numero in range(10000, 50000):
        for auxiliar in range(2, numero):
            if numero % auxiliar == 0:
                break
        else:
            primos.append(numero)
    return random.choice(primos), random.choice(primos)
# Totiente de euler
def phi(p, q): 
    return (p - 1) * (q - 1)



