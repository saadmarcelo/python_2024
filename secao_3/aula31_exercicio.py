"""
Faca um programa que peca ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar. Caso o usuario nao digite um numero 
inteiro, informe que nao é um numero inteiro.
"""

numero = input("Entre com um numero inteiro: ")

if numero.isdigit():

    numero_int = int(numero)
    par_impar = (numero_int % 2) == 0
    if par_impar:
        print(f"O numero {numero_int} é par")
    else:
        print(f"O numero {numero_int} é impar")
else:
    print("Voce nao digitou um numero inteiro")

"""
faca um programa que pergunte a hora do usuario e, baseando-se no horario descrito,
exiba a saudacao apropriada . Ex:
bom dia 0-11, Boa tarde 12-17 e Boa noite 18 as 23
"""

hora = input("Digite a hora em numeros inteiros: ")
try:
    hora_int = int(hora)

    if 0 <= hora_int <= 11:
        print("Bom dia")
    elif 12 <= hora_int <= 17:
        print("Boa tarde")
    elif 18 <= hora_int <= 23:
        print("Boa noite")
    else:
        print("Nao é uma hora válida")
except:
    print("Por favor, digite apenas numeros inteiros")

"""

Faca um programa que peca o primeiro nome do usuario. Se o nome tiver 4 letras ou
menos escreve "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"seu nome é normal"; mairo que 6 escreva "seu nome é muito grande"
"""

nome = input("Ente com o primeiro nome: ")
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print("Seu nome é pequeno")
elif tamanho_nome <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
