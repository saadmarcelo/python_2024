"""Validar CPF"""

import re
import sys

entrada = input("CPF: ")

# cpf_enviado_usuario = (
#     "746.824.890-70".replace(".", "").replace(" ", "").replace("-", "")
# )

cpf_enviado_usuario = re.sub(r"[^0-9]", "", entrada)
entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print("Voce enviou dados sequenciais.")
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
primeiro_digito = (resultado_digito_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print(primeiro_digito)


dez_digitos = nove_digitos + str(primeiro_digito)
contador_regressivo_2 = 11


resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
segundo_digito = (resultado_digito_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0
print(segundo_digito)

cpf_gerado_pelo_calculo = f"{nove_digitos}{primeiro_digito}{segundo_digito}"

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f"{cpf_enviado_usuario} é valido")
else:
    print("CPF inválido")
