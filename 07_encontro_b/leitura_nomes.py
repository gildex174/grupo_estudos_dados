nomes = []

with open("nomes.txt", "r") as file:
    lines  = file.readlines()

for line in lines:
    nomes.append(line.rstrip())

for nome in sorted(nomes):
    print(f"Olá, {nome}!")
