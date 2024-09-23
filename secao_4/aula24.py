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
