# FUNCION PARA OBTENER PROMEDIO DE LISTA DE NUMEROS
def promedio(numeros):
    total = 0
    for numero in numeros:
        total = total + numero

    prom = float(total) / len(numeros)

    return prom

# MAIN
cantidad = input("Cantidad de numeros a ingresar: ")

numeros = list()

loop = range(cantidad + 1)
while loop.pop():
    numeros.append(input("Numero: "))


print(promedio(numeros))