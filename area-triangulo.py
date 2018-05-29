# CALCULA AREA DE UN TRIANGULO
def areaTriangulo(base1, altura):
    resultado = float(base1 * altura) / 2

    return resultado


# MAIN
def main():
    print("Programa para obtener area de un triangulo\n")
    base1 = input("Medida de la base en cm: ")
    altura = input("Medida de la altura en cm: ")

    print("El area del triangulo es: " + str(areaTriangulo(base1, altura)) + " cm2")

main()