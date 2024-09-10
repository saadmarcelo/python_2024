"""lista de listas e sues indices"""

salas = [
    [
        "Maria",
        "Helena",
    ],
    [
        "Elaine",
    ],
    ["Luiz", "João", "Eduarda", (0, 10, 20, 30, 40)],
]

# print(salas)
# print(salas[1][0])
# print(salas[2][1])
# print(salas[0][0])
# print(salas[2][3][3])


for sala in salas:
    for aluno in sala:
        print(aluno)
