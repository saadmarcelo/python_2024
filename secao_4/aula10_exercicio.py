"""
Exercicios
crie funcoes que duplicam, triplicam e quadruplicam
o numero recebido como parematro
"""

# def duplicar(num):
#     return num * 2
#
#
# def triplicar(num):
#     return num * 3


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador

    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
