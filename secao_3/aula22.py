nome = "Marcelo"

print(nome[2])
print(nome[-5])
print("r" in nome)
print("z" in nome)
print(10 * "-")
print("r" not in nome)
print("z" not in nome)


nome = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} este em {nome}")
else:
    print(f"{encontrar} nao esta em {nome}")
