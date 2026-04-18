def quadrado(num):
    return num + num 


def main():

    numero_usuario = int(input("Diga um número: \n"))

    print(f'Número ao quadrado: {quadrado(numero_usuario)}')


if __name__ == "__main__":
    main()