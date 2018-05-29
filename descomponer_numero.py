# CALCULA MILLARES, CENTENAS, DECENAS Y UNIDADES DE UN NUMERO
def obtenerMillares(numero):
    return int(numero) / 1000

def obtenerCentenas(numero):
    return (numero - (obtenerMillares(numero) * 1000)) / 100

def obtenerDecenas(numero):
    return (numero - int(obtenerMillares(numero)*1000 + obtenerCentenas(numero)*100)) / 10

def obtenerUnidades(numero):
    return (numero - (obtenerMillares(numero) * 1000 + obtenerCentenas(numero) * 100 + obtenerDecenas(numero) * 10))

# MAIN
def main():
    print("Programa para calcular las decenas y unidades de un numero")
    numero = input("Ingresa el numero a calcular: ")

    print("Los Millares de " + str(numero) + " son: " + str(obtenerMillares(numero)))
    print("Las Centenas de " + str(numero) + " son: " + str(obtenerCentenas(numero)))
    print("Las Decenas de " + str(numero) + " son: " + str(obtenerDecenas(numero)))
    print("Las Unidades de " + str(numero) + " son: " + str(obtenerUnidades(numero)))


main()