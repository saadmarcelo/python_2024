lista = [10, 20, 30, 40]
lista[2] = 300
del lista[2]
print(lista)
lista.append(50)
lista.pop()  # remove o ultimo item da lista no momento
lista.pop(2)  # remove o item do indice 2
lista.append(60)
print(lista)
