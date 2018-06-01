def Fibonacci(i):
    contador = 0
    serie = list()
    while contador != i:
        if (contador == 0) | (contador == 1):
            serie.append(contador)
        else:
            serie.append( serie[contador - 2] + serie[contador - 1] )

        contador = contador + 1
    return serie

def main():
    print("Serie de Fibonacci")
    numero = input("Ingresa el numero de iteraciones que deseasmostrar: ")

    print("Resultado de la serie: " + str(Fibonacci(numero)))

main()