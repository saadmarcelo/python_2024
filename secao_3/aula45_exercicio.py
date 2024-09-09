import os

palava_secreta = "perfume"
letras_acertadas = ""
tentativas = 0
while True:
    letra_digitada = input("Digite uma letra: ")
    tentativas += 1
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue
    if letra_digitada in palava_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""
    for letra_secreta in palava_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print("Palavra formada", palavra_formada)
    if palavra_formada == palava_secreta:
        os.system("clear")
        print("VOCE GANHOU!! PARABENS! ")
        print("A palavra era", palava_secreta)
        print(f"Voce tentou {tentativas}x")
        letras_acertadas = ""
        tentativas = 0
