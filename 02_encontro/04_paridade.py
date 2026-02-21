def numero_par(num):

    return num % 2 == 0

    # return True if num % 2 == 0 else False

    # if num % 2 == 0:
    #     return True  # Variável Booleana
    # else:
    #     return False


def main():
    x = int(input("Diga um número: \n"))

    if numero_par(x):
        print("X é par!!")
    else:
        print("X é ímpar!!")


main()
