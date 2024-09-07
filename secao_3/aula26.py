nome = input("Entre com o seu nome: ")
idade = input("Entre com a sua idade: ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if " " in nome:
        print("Seu nome contem espaço")
    else:
        print("Seu nome nao contem espaco")
    print(f"O seu nome tem {len(nome)} caracteres")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, voce deixou campos vazios")
