
def potencia_numero(num, potencia):
    quadrado = pow(num, potencia) 

    print(f"O número ao quadrado é {quadrado}")

    return quadrado

def main():
    x  = int(input("Diga-me um número: "))
    y = int(input("Diga a potência:"))
    x_quadrado = potencia_numero(num=x, potencia=y)

    print(f"Resultado da operação: {x_quadrado - 5}")



main()