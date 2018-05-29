# FUNCION PARA VERIFICAR SI LA PALABRA1 ES PALINDROMA CON LA PALABRA2
def palindroma(palabra1, palabra2): 
    i = len(palabra1) - 1

    for caracter in palabra2:
        if caracter != palabra1[i]:
            return False
        i = i-1
    
    return True

# MAIN
print("Programa para detectar si una palabra es palindroma")

cadena1 = raw_input("Escribe palabra 1: ")
cadena2 = raw_input("Escribe palabra 2: ")

if(palindroma(cadena1, cadena2)):
    print("Es palindroma")
else:
    print("No es palindroma")