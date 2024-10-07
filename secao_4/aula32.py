"""
Generator expression, Iterables e Iterators em python
"""

import sys

iterable = ["Eu", "tenho", "__iter__"]
iterator = iter(iterable)
generator = (
    n for n in range(10000)
)  # é uma funcao q salve pausar, entregua um valor por vez
lista = [n for n in range(10000)]
print(sys.getsizeof(generator))
print(sys.getsizeof(lista))
