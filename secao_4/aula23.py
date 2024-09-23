"""
Empacotamento e desempacotamento de dicionarios
"""

a, b = 1, 2
a, b = b, a
print(a, b)

# pessoa = {
#     "nome": "Aline",
#     "sobrenome": "Souza",
# }
# a, b = pessoa
# print(a, b)
#
# c, d = pessoa.values()
# print(c, d)


pessoa = {
    "nome": "Aline",
    "sobrenome": "Souza",
}

dados_pessoa = {
    "idade": 16,
    "altura": 1.7,
}

pessoas_completa = {**pessoa, **dados_pessoa}

print(pessoas_completa)


# kwargs - keyword arguments (argumntos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print("NAO NOMEDOS: ", args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(1, 2, nome="joana", qlq=123)
mostro_argumentos_nomeados(**pessoas_completa)
