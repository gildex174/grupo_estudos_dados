def numero_inteiro(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("Número inválido")
        else:
            return x





def main():

    numero_usuario_1 = numero_inteiro(prompt = "Diga um número:")
    numero_usuario_2 = numero_inteiro(prompt = "Diga outro número:")

    print(f"A multiplicação dos valores: {numero_usuario_1 * numero_usuario_2}")

main()
