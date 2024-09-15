"""
    Exercicio com funcoes
    crie uma funcao que multilplica todos os argumentos
    nao nomeados recebidos
    retorne o valor total para uma variavel e motre o valor da variavel
"""


def multi(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


valor = multi(4, 9)
print(valor)
