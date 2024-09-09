lista = [10, 20, 30, 40]

lista.append("Marcelo")
nome = lista.pop()
lista.append(12333)
del lista[-1]  # apaga o item de indice -1 (ultimo item da lista)
# lista.clear()  # limpar a lista
lista.insert(0, 5)


print(lista, nome)
