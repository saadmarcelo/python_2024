"""
Operadore uteis
união | união (union) - Une
intersecção & (intersection) - Itens presente em ambos
diferença - Itens presents apenas no set da esquerda
diferença simetrica ^ - Itens que não estao em ambos

"""

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 ^ s2
print(s3)
print(s4)
print(s5)
print(s6)
