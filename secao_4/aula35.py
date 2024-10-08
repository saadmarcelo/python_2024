"""
Try, except, else e finally
"""

a = 18
# b = 0
try:
    print("linha 1")
    c = a / b
    print("linha 2")
except ZeroDivisionError:
    print("Dividiu por zero")
except NameError:
    print("a variavel nao esta definida")
except Exception:
    print("Erro desconhecido")
print("Continuar")
