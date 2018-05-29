import copy

# DETERMINAR SI UN NUMERO ES PRIMO O NO
def esPrimo(numero):
    i = 2

    while(i <= numero):
        # Si el numero es divisible entre otro numero diferente de 1 y el mismo => es falso
        if ((numero % i) == 0) & (numero != i):
            return False
        # Si el numero es divisible entre el mismo => es verdadero
        elif ((numero % i) == 0) & (numero == i):
            return True
        i = i + 1


# MAIN
def main():
    print("Programa para determinar si un numero es primo")
    numero = input("Ingresa un numero: ")

    if(esPrimo(numero)):
        print("El numero " + str(numero) + " es primo!")
    else:
        print("El numero " + str(numero) + " no es primo")


main()