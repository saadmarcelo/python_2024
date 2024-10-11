import importlib

import aula40_m

print(aula40_m.variavel)

for i in range(10):
    importlib.reload(aula40_m)
    print(i)

print("fim")
