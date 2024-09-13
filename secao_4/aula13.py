"""
Metodos uteis dos dicionarios em python
len - quantas chaves
keys - iteráveis com as chaves
values - iteravel com os valores
items - iteraveis com chaves e valores
setdefault - adiciona valor se a chave nao existe
copy - retorna uma copia rasa (shallow copy)
get - obtem a chave
pop - Apaga um imte com a chave especificada ( del )
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario com outro
"""

pessoa = {
    "nome": "Marcelo",
    "sobrenome": "Saad",
}

pessoa.setdefault(
    "idade", 0
)  # se o map idade nao existir ele cria com o valor padrao de 0 , se o valor exisir ele imprime o valor salvo
print(pessoa["idade"])

print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

for chave in pessoa:
    print(chave)
for valor in pessoa.values():
    print(valor)
for chave, valor in pessoa.items():
    print(chave, valor)
