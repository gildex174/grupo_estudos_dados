import re

nome =  input("Diga seu nome: ").strip()

nome_regex = re.search(r"^(.+), ?(.+)$", nome)

if nome_regex:
    print(f"Olá, {nome_regex.group(2)}")
else:
    print("Erro")