from calculadora import quadrado

def teste_positivos():

    assert quadrado(2) == 4
    assert quadrado(3) == 9

def teste_negativos():
    assert quadrado(-2) == 4
    assert quadrado(-3) == 9

def teste_zero():
    assert quadrado(0) == 0

def main():
    teste_positivos()
    teste_negativos()
    teste_zero()

if __name__ == "__main__":
    main()