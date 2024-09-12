"""
Dicionarios em python
"""

pessoa = {
    "nome": "Marcelo",
    "sobrenome": "Saad",
    "idade": 41,
    "altura": 1.71,
    "enderecos": [
        {"rua": "tal tal", "numero": 123},
        {"rua": "outra rua", "numero": 321},
    ],
}

print(pessoa, type(pessoa))
print(pessoa["altura"])
