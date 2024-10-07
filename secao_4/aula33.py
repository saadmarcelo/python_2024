"""
Introdução às generator functions em python
"""


# def generator(n=0):
#     yield 1  # Pausar
#     print("Continuando...")
#     yield 2  # Pausar
#     print("Mais uma...")
#     yield 3  # Pausar
#     print("Vou terminar...")
#     return "ACABOU"
def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(n=0)
for n in gen:
    print(n)
