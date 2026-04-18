nome = input("Nome: \n")

with open("nomes.txt", "a") as file:
    file.write(f"{nome}\n")
