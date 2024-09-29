"""
List comprehension em python
"""

# print(list(range(10)))

# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

lista = [1 for numero in range(10)]
lista1 = [numero for numero in range(10)]
print(lista)
print(lista1)


lista2 = [numero * 2 for numero in range(10)]
print(lista2)

# Mapeamento de dados em list
produtos = [
    {
        "nome": "p1",
        "preco": 20,
    },
    {
        "nome": "p2",
        "preco": 10,
    },
    {
        "nome": "p3",
        "preco": 30,
    },
]
novos_produtos = [{**produto, "preco": produto["preco"] * 1.05} for produto in produtos]
print(novos_produtos)
