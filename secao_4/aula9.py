"""Clousure e funcoes que retornam outras funcoes"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}"

    return saudar


s1 = criar_saudacao("Bom dia")
s2 = criar_saudacao("Boa Noite")

print(s1("Saad"))
print(s2("Laura"))
