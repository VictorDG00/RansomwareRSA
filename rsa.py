import random
# criar 2 numero primos

def gerarNP():
    primos = []
    for numero in range(2, 600):
        for auxiliar in range(2, numero):
            if numero % auxiliar == 0:
                break
        else:
            primos.append(numero)
    return random.choice(primos), random.choice(primos)
q , p = gerarNP()
print(q,p)
