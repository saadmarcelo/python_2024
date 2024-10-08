"""
try, except, else e finally
"""

try:
    print("Abrir o arquivo")
    8 / 0
except ZeroDivisionError:
    print("Dividiu por zero")
finally:
    print("Fechar arquivo")
