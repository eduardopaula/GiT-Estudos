import random

numeros = set()

while len(numeros) < 6:
    x = random.randint(1,60)
    numeros.add(x)

print(numeros)
