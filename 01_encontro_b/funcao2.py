def eleva_potencia(numero, potencia):

    print(numero**potencia)
    return numero**potencia

def main():

    usuario_numero = int(input("Diga um número: "))
    usuario_potencia = int(input("Diga sua potencia: "))

    numero_elevado = eleva_potencia(numero = usuario_numero, potencia=usuario_potencia)

    print(numero_elevado - 4)

main()