def sum_eo(n, t):
    soma = 0
    if t.casefold() == "e":
        for numero in (range(0, n)):
            if numero % 2 == 0:
                soma += numero
        return soma
    elif t.casefold() == "o":
        for numero in (range(0, n)):
            if numero % 2 != 0:
                soma += numero
        return soma
    else:
        return -1


print(sum_eo(10, "spam"))
