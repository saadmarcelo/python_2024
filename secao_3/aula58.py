""" split e join """

frase = "      Olha so que ,     coisa interessante      "

lista_palavras = frase.split()
lista_frases_cruas = frase.split(",")
print(lista_palavras)
print(lista_frases_cruas)

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases)

frases_unidas = "-".join(lista_frases)
print(frases_unidas)
