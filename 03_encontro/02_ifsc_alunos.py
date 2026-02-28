alunos = [
    {"nome": "Brastemp", "curso": "biomol", "origem": "sao carlos"},
    {"nome": "Fapesp", "curso": "biomol", "origem": "passos"},
    {"nome": "Gildo", "curso": "fiscomp", "origem": "fortaleza"},
    {"nome": "Sofia", "curso": "fisica", "origem": "resende"},
]

for aluno in alunos:
    # print(aluno)
    print(aluno["nome"], aluno["curso"], aluno["origem"], sep="| ")
