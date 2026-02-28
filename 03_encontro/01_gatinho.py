def meow(n):
    for _ in range(n):
        print("meow")


def receba_numero():
    while True:
        numero_usuario = int(input("Diga um número:"))

        if numero_usuario <= 0:
            continue
        else:
            return numero_usuario


def main():
    num_usuario = receba_numero()
    meow(num_usuario)


main()
