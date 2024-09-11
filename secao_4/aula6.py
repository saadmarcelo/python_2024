"""Args - argumentos nao nomeados"""

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


# def soma(x, y):
#     return x + y


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 50
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))
