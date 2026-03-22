def ola(nome):
    print(f"Olá, {nome}")

def ate_mais(nome):
    print(f"Até mais, {nome}")

def main():
    nome = input("Diga seu nome: \n")
    ola(nome)
    ate_mais(nome)

if __name__ == "__main__":
    main()