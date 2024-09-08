nome = "Marcelo Saad"
tamanho_nome = len(nome)

print(tamanho_nome)
print(nome)

indice = 0
novo_nome = ""
while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += f"*{letra}"
    indice += 1

novo_nome += "*"
print(novo_nome)
