"""Escopo de funcoes em python"""

x = 1


def escopo():
    x = 10

    def outra_funcao():
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)
