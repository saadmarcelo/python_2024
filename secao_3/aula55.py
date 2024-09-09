lista = ["Maria", "Helena", "Luiz"]
lista.append("João")


for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)
