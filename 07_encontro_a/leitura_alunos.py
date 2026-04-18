alunos = []

with open("alunos.csv", "r") as file:
    for line in file:
        nome, curso = line.rstrip().split(",")

        aluno = {"nome": nome, "curso":curso}
        alunos.append(aluno)


for aluno in sorted(alunos, key=lambda aluno:aluno["curso"]):
    print(f"{aluno['nome']} faz o curso {aluno['curso']}")
