import random

class Fuvest:
    
    cursos = ["lic", "fisica", "biomol"]

    @classmethod
    def selecionar_curso(cls, nome):

        print(f"{nome} irá fazer {random.choice(cls.cursos)}!")

# fuvest = Fuvest()

Fuvest.selecionar_curso("Gildo")