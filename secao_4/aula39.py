"""
Entendendo os seus proprios modulos python
o primeiro modulo executado chama-se __main__
vode pode importar outro modulo inteiro ou parte do modulo
o python conehce a pasta onde o __main__ esta e as pastas abaixo dele
Ele nao reconhece pastas e modulos acima do __main__ por padrao
o python conhece todos os modulos e pacotes presentes no caminho do sys.path
"""

import aula39_m

print("Este modulo se chama", __name__)
