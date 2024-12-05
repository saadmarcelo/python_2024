# combinations, permutations e product - itertools
# Combinação - Ordem nao importa - iteravel + tamanho do grupo
# Permutacao - ordem importa
# Produto - Ordem importa e repete valores unicos
from itertools import combinations


def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()


pessoas = [
    "João",
    "Joana",
    "Luiz",
    "Leticia",
]
camisetas = [
    ["preta", "Branca"],
]

print_iter(combinations(pessoas, 2))
