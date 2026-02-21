# Pergunte o nome do usuário
nome = input("Qual é o seu nome ??\n")
nome = nome.strip()
nome = nome.title()
primeiro_nome, segundo_nome = nome.split()
# Mostre a resposta
print(f"Olá, {nome}", end="\n")
print(f"Olá, {primeiro_nome}", end="\n")