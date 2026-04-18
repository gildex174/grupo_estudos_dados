nome = input("Diga seu nome: ")

with open("nomes.txt", "a") as file:
    file.write(f"{nome}\n")

