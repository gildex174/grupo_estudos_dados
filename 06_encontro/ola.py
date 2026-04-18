def ola(nome="mundo"):

    return f"Olá, {nome}!"


def main():

    nome_usuario = input("Diga seu nome: \n")
    print(ola(nome_usuario))

if __name__ == "__main__":
    main()