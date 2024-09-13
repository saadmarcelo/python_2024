"""
Manipulando chaves e valores em dicionarios
"""

pessoa = {}
chave = "nome_completo"


pessoa[chave] = "Marcelo Saad"
pessoa["sobrenome"] = "Silva"

print(pessoa)
print(pessoa[chave])
del pessoa["sobrenome"]

pessoa[chave] = "Laura Saad"
print(pessoa[chave])
print(pessoa)

if pessoa.get("sobrenome") is None:
    print("Nao existe")
else:
    print(pessoa["sobrenome"])
