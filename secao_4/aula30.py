"""
dir, hasattr e getattr em python
"""

string = "Marcelo"
metodo = "upper"

if hasattr(string, metodo):
    print("Existe upper")
    print(string.upper())
    print(getattr(string, metodo)())
else:
    print("Não existe o metodo", metodo)
