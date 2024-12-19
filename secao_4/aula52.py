# combinations, permutations e product - itertools
# Combinação - Ordem nao importa - iteravel + tamanho do grupo
# Permutacao - ordem importa
# Produto - Ordem importa e repete valores unicos
from itertools import combinations, permutations, product


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
    ["p", "m"],
    ["masculino", "feminino"],
]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
