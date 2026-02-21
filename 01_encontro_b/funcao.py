def ola(nome_usuario = "mundo"):
    print("Olá, " + nome_usuario)

def main():
    nome = input("Diga o seu nome: ")
    ola(nome_usuario=nome)
main()