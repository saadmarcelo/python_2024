print(1234)
print(456)

numero_str = input("Vou dobrar o numero que vc colocar: ")

try:
    numero_float = float(numero_str)
    print("FLOAT:", numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2:.2f}")
except:
    print("Isso nao é um numero")


# if numero_str.isdigit():
#    numero_float = float(numero_str)
#    print(f"O dobro de {numero_float} é {numero_float * 2:.2f}")
# else:
#    print("Isso nao é um numero")
