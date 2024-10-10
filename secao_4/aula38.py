"""
Modulos padrao do python (import, from as e *)
inteiro - import nome_modulo
Vantagens : voce tem o namespace do modulo
desvantagem: nomes grandes
"""

# import sys
#
# print(sys.platform)


"""
partes - from nome_modulo importe objeto1, objeto2
Vantagens: nomes pequenos
desvantagem: Sem o namespace do modulo
"""

from sys import exit, platform

print(platform)
