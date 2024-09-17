"""
sets - conjuntos em python

"""

s1 = set()  # set vazio
s2 = {"Marcelo", 1, 2, 3}  # set com dados

print(s1)
print(s2)

# sao iteraveis
# nao possuem valores repetidos
s3 = {1, 2, 3, 3, 3, 3, 3, 1}
print(s3)

# Metodos uteis
# add, update, clear, discard

s4 = set()
s4.add("Marcelo")
s4.add(1)
s4.update(("Ola mundo", 1, 2, 3, 4, 5))
# s4.clear() # limpar o set
s4.discard("Ola mundo")  # remove o valor do set
print(s4)
