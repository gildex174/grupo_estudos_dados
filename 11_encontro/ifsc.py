class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Aluno(Pessoa):
    def __init__(self,nome, curso):
        
        self.curso = curso
        super().__init__(nome)

    ...

class Professor(Pessoa):

    def __init__(self, nome, area_pesquisa):
        super().__init__(nome)
        self.area_pesquisa = area_pesquisa

    ...


pessoa_1 = Pessoa("Gildo")

pessoa_2 = Aluno("Brastemp", "Biomol")

pessoa_3 = Professor("Fapesp", "Biofotonica")


print(pessoa_1.nome)

print(pessoa_2.nome, pessoa_2.curso)

print(pessoa_3.nome, pessoa_3.area_pesquisa)