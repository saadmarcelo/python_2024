""" criando a lista e usando a funcao enumarate"""

lista = ["Maria", "Helena", "Luiz"]
lista.append("João")

# for item in enumerate(lista):
#    indice, nome = item
#    print(indice, nome)

for indice, nome in enumerate(lista):
    print(indice, nome)
