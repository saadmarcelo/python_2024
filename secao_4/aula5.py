"""retorno de valores da funcao"""


def soma(x, y): ...


variavel = soma(1, 2)
print(variavel)


def soma1(x, y):
    return x + y


soma_1 = soma1(2, 2)
soma_2 = soma1(3, 3)
print(soma_1 + soma_2)
