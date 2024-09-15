"""
Metodos uteis dos dicionarios em python
"""

p1 = {
    "nome": "Marcelo",
    "sobrenome": "Saad",
}

# print(p1.get("nome"))
# print(p1.get("nome", "Não existe"))
#
# nome = p1.pop("nome")  # pega o valor da chave nome mas apaga do map
# print(nome)
# print(p1)
#
#
# ultima_chave = p1.popitem()  # apaga o ultimo item do map
# print(ultima_chave)
# print(p1)

p1.update(
    {
        "nome": "laura",
        "idade": 4,
    }
)
print(p1)
