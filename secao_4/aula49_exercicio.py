"""
Exercicio - Unir listas
crie uma funcao zipper ( como o zipper de roupas )
o trabalho dessa funcao sera unir duas listas na ordem
use todos os valores da menro lista
ex:
    ['Salvador', 'Ubatuba', 'Belo Horizonte']
    ['BA', "SP", 'MG', 'RJ']
    resultado
    [('salvador', 'BA'), ("Ubatuba", 'SP'), ("Belo Horizonte", 'MG')]
"""

#
# def zipper(l1, l2):
#     intervalo_maximo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo_maximo)]
#
#
# l1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
# l2 = ["BA", "SP", "MG", "RJ"]
#
# print(zipper(l1, l2))
from itertools import zip_longest

l1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
l2 = ["BA", "SP", "MG", "RJ"]
# funcao zip faz a mesma coisa q o codigo acima mas ele retorna um iterator

print(list(zip(l1, l2)))
print(
    list(zip_longest(l1, l2, fillvalue="SEM CIDADE"))
)  # funcao zip_longest imprime os valores da maior lista
