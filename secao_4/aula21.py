"""
Funcao lambda em python
"""

# lista = [
#     4,
#     32,
#     1,
#     34,
#     5,
#     6,
#     6,
#     21,
# ]
# lista.sort()  # ordena a lista
# # lista.sort(reverse=True) # Ordem decrescente
# # sorted(lista) # cria uma copia rasa da lista
#
# print(lista)

lista1 = [
    {"nome": "Luiz", "sobrenome": "miranda"},
    {"nome": "Maria", "sobrenome": "Oliveira"},
    {"nome": "Daniel", "sobrenome": "Silva"},
    {"nome": "Eduardo", "sobrenome": "Moreira"},
    {"nome": "Aline", "sobrenome": "Souza"},
]


# def ordena(item):
#     return item["sobrenome"]


# lista1.sort(key=ordena)

# lista1.sort(key=lambda item: item["nome"])


def exibir(lista1):
    for item in lista1:
        print(item)


l1 = sorted(lista1, key=lambda item: item["nome"])
l2 = sorted(lista1, key=lambda item: item["sobrenome"])

exibir(l1)
print()
exibir(l2)
