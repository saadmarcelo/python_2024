"""
Metodos uteis dos dicionarios em python
copy - retorna uma copia rasa (shallow copy)
get - obtem a chave
pop - Apaga um imte com a chave especificada ( del )
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario com outro
"""

import copy  # modulo para fazer a copia completa do map

d1 = {
    "c1": 1,
    "c2": 2,
}
d2 = d1.copy()  # Faz uma copia rasa do map, nao vem o subniveis

d2["c1"] = 1000
print(d1)
print(d2)


d10 = {"c1": 1, "c2": 2, "l1": [0, 1, 2]}
d20 = copy.deepcopy(d10)  # Faz uma copia completa do map

d20["c1"] = 1000
d20["l1"][1] = 9999999
print(d10)
print(d20)
