# Ejercicio: Crear una clase con los parametros basicos de una lista y el funcionamiento de la misma
class Lista:
    class Nodo:
        def __init__(self):
            pass

        #def __init__(self, contenido, siguiente):
        #    self.contenido = contenido
        #    self.siguiente = siguiente

        def setContenido(self, contenido):
            self.contenido = contenido

        def setSiguiente(self, siguiente):
            self.siguiente = siguiente

        def getContenido(self):
            return self.contenido

        def getSiguiente(self):
            return self.siguiente
        


    nodoInicial = None
    longitud = 0

    def __init__(self):
        pass

    def agregar(self, contenido):
        if self.nodoInicial == None:
            self.nodoInicial = self.Nodo()

            self.nodoInicial.setContenido(contenido)
            self.nodoInicial.setSiguiente(None)
        else:
            nodoTemp = self.Nodo()
            nodoTemp.setContenido(contenido)
            nodoTemp.setSiguiente(None)

            nodo = self.ultimoNodo()
            nodo.setSiguiente(nodoTemp)


        self.longitud = self.longitud + 1


    def eliminar(self, indice):
        i = 0
        nodo = self.nodoInicial
        while i != indice - 1:  # Asumiendo que los indices van de 0, 1, 2, etc...
            nodo = nodo.getSiguiente()
            i = i + 1
            if(nodo == None):
                return False
        nodoEliminar = nodo.getSiguiente()
        nodoSiguiente = nodoEliminar.getSiguiente()
        nodo.setSiguiente(nodoSiguiente)
        self.longitud = self.longitud - 1

        return True

    def verContenido(self, indice):
        i = 0
        nodo = self.nodoInicial
        while i != indice:
            nodo = nodo.getSiguiente()
            i = i + 1

        return nodo.getContenido()

    def getNodo(self, indice):
        i = 0
        nodo = self.nodoInicial
        while i != indice:
            nodo = nodo.getSiguiente()
            i = i + 1

        return nodo

    def getLongitud(self):
        return self.longitud

    def ultimoNodo(self):
        nodo = self.nodoInicial

        while nodo.getSiguiente() != None:
            nodo = nodo.getSiguiente()

        return nodo

    # Funcionalidad extra de una pila
    def pop(self):
        if(self.getLongitud() <= 0):
            # no se puede eliminar nada si la lista o pila ya esta vacia(ERROR AL HACER POP)
            return False
        if(self.getLongitud() == 1):
            self.nodoInicial = None
            self.longitud = 0
            return True
        else:
            # Se busca un penultimo nodo de la lista
            nodo = self.getNodo(self.getLongitud() - 2)
            # Se accede al ultimo nodo por medio del metodo setSiguiente() del penultimo nodo
            # y se elimina agregando None para que ya no haga referencia al ultimo nodo
            nodo.setSiguiente(None)
            # Al tener la pila un nodo menos, se ajusta su longitud de lista o pila
            self.longitud = self.longitud - 1
            return True
    
    def push(self, contenido):
        self.agregar(contenido)

# MAIN
def main():
    print("===========Ejemplo Listas==============")
    pruebaLista()
    print("===========Ejemplo pilas================")
    pruebaPila()

def pruebaPila():
    pilaEjemplo = Lista()
    pilaEjemplo.push("Hola")
    pilaEjemplo.push("Mundo!!!")
    pilaEjemplo.push("Me")
    pilaEjemplo.push("gusta")
    pilaEjemplo.push("mucho")
    pilaEjemplo.push("la")
    pilaEjemplo.push("programacion")

    # verContenido
    for i in range(pilaEjemplo.getLongitud()):
        print("Elemento" + str(i) + ": " + str(pilaEjemplo.verContenido(i)))

    print("")
    for i in range(5):          # los numeros del rango se pueden cambiar para probar que se hace pop correctamente
        if pilaEjemplo.pop():
            print("POP EXITOSO!")
        else:
            print("PILA VACIA, ERROR POP")
    
    # Agraga nuevamente para verificar que se conectan los nodos
    pilaEjemplo.push("Python")
    pilaEjemplo.push("es")
    pilaEjemplo.push("genial!")
    print("\nDespues del pop\n") # al hacer 3 pop, se elimina "mucho", "la", "programacion"


    # verContenido
    for i in range(pilaEjemplo.getLongitud()):
        print("Elemento" + str(i) + ": " + str(pilaEjemplo.verContenido(i)))

def pruebaLista():
    #Agregar
    listaEjemplo = Lista()
    listaEjemplo.agregar("Hola")
    listaEjemplo.agregar("Mundo!!!")
    listaEjemplo.agregar("Me")
    listaEjemplo.agregar("gusta")
    listaEjemplo.agregar("mucho")
    listaEjemplo.agregar("la")
    listaEjemplo.agregar("programacion")

    # verContenido
    for i in range(listaEjemplo.getLongitud()):
        print("Elemento" + str(i) + ": " + str(listaEjemplo.verContenido(i)))

    # getLongitud
    print("\nExisten " + str(listaEjemplo.getLongitud()) + " elementos en la lista\n")

    # Eliminar
    indice = 4
    if listaEjemplo.eliminar(indice): # Elimina nodo en indice 4 "mucho"
        print("Se ha eliminado nodo en indice " + str(indice))
    else:
        print("El nodo no se ha eliminado correctamente")

    print("\nMostrar elementos nuevamente: ")

    # verContenido
    for i in range(listaEjemplo.getLongitud()):
        print("Elemento" + str(i) + ": " + str(listaEjemplo.verContenido(i)))

    # getLongitud
    print("\nExisten " + str(listaEjemplo.getLongitud()) + " elementos en la lista")

main()
