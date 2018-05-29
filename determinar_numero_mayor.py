# DETERMINA EL NUMERO MAYOR ENTRE DOS NUMERO
def mayorValor(numero1, numero2):
    if numero1 < numero2:
        return numero2
    else:
        return numero1


def main():
    print("Programa para determinar el numero mayor entre dos numeros")
    num1 = input("Numero 1: ")
    num2 = input("Numero 2: ")

    print("El numero mayor es: " + str(mayorValor(num1, num2)))

main()