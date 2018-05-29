import copy

# INVERTIR NUMERO POSITIVO, EJEMPLO: 123 -> 321
def invertirNumero(numero):
    numeroStr = str(numero)
    numeroInvertido = list()
    
    contador = len(numeroStr) - 1

    while contador >= 0:
        numeroInvertido.append(numeroStr[contador])
        contador = contador - 1

    return int("".join(numeroInvertido))

# MAIN
def main():
    print("Programa para invertir orden de numero positivo")
    numero = input("Ingresa un numero entero positivo: ")

    numeroInvertido = invertirNumero(numero)

    print("El numero " + str(numero) + " invertido es: " + str(numeroInvertido))

main()