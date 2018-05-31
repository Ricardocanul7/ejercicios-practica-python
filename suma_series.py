# DADO UN NUMERO N, CALCULA LA SUMA DE LA SERIE 1 + 2 + 3 + ... + N
def serie1(n):
    i = 0
    suma = 0
    while i != n:
        i = i + 1
        suma = suma + i

    return suma

# DADO UN NUMERO N, CALCULA LA SUMA DE LA SERIE 1 + 1/2 + 1/3 + ... + 1/N
def serie2(n):
    i = 0
    suma = 0
    
    while i != n:
        i = float(i) + 1
        suma = suma + (1 / i)
    
    return suma

# DADO UN NUMERO N, CALCULA LA SUMA DE LA SERIE 1 + 1/2! + 1/3! + ... + 1/N!
def serie3(n):
    i = 0
    suma = 0
    
    while i != n:
        i = float(i) + 1
        suma = suma + (1 / float(factorial(i)))

    return suma

def factorial(n):
    factorial = 1
    i = 0
    while i != n:
        i = i + 1
        factorial = factorial * i

    return factorial

def main():
    print("Series")
    numero = input("Ingresa un numero N: ")

    print("\nResultado de serie1: " + str(serie1(numero)))
    print("Resultado de serie2: " + str(serie2(numero)))
    print("Resultado de serie3: " + str(serie3(numero)))
    print("Resultado del factorial: " + str(factorial(numero)))

main()