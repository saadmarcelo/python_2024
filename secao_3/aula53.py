nomes = ["Maria", "Helena", "Luiz"]
nome1, nome2, nome3 = nomes
print(nome2)


nome_1, *_ = ["Maria", "Helena", "Luiz"]
print(nome_1)
_, _, nome, *_ = ["Maria", "Helena", "Luiz"]
print(nome)
