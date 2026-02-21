# Pergunte o nome do usuário
nome = input("Qual é o seu nome??\n")

nome = nome.strip().title()
primeiro, segundo = nome.split()
# Diga olá para ele

print(f"Olá, {segundo}")