""" lista com try/except """

import os

lista = []

while True:
    print("Selecione uma opção")
    opcao = input("Voce quer [i]nserir, [a]pagar ou [l]istar: ").lower()

    if opcao.startswith("i"):
        os.system("clear")
        valor = input("Valor: ")
        lista.append(valor)

    elif opcao.startswith("a"):
        os.system("clear")
        for i, valor in enumerate(lista):
            print(i, valor)
        indice_str = input("Escolha o índice para apagar: ")

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print("Por favor digite numero int.")
        except IndexError:
            print("Indice não existe na lista")
    elif opcao.startswith("l"):
        os.system("clear")
        if len(lista) == 0:
            print("Nada para listar")

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print("Entrar com uma opcao valida")
        continue
