"""
    Exercicio com funcoes
    crie uma funcoa que multilplica todos os argumentos
    nao nomeados recebidos
    retorne o valor total para uma variavel e motre o valor da variavel
"""


def multi(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


valor_mult = multi(2, 3, 4)
print(valor_mult)

"""
    crie uma funcao fala se um numero é par ou impar
    retorne se o numer é par ou impar
"""


def impar_par(x):
    if x % 2 == 0:
        return f"{x=} é par"
    return f"{x=} é impar"


print(impar_par(11))
print(impar_par(5))
print(impar_par(20))
