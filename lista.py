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
        pass

    def verContenido(self, indice):
        i = 0
        nodo = self.nodoInicial
        while i != indice:
            nodo = nodo.getSiguiente()
            i = i + 1
        
        return nodo.getContenido()

    def getLongitud(self):
        return self.longitud

    def ultimoNodo(self):
        nodo = self.nodoInicial

        while nodo.getSiguiente() != None:
            nodo = nodo.getSiguiente()
        
        return nodo


def main():
    listaEjemplo = Lista()
    listaEjemplo.agregar("Hola")
    listaEjemplo.agregar("Mundo!!!")
    listaEjemplo.agregar("Me")
    listaEjemplo.agregar("gusta")
    listaEjemplo.agregar("mucho")
    listaEjemplo.agregar("la")
    listaEjemplo.agregar("programacion")

    for i in range(listaEjemplo.getLongitud()):
        print("Elemento" + str(i) + ": " + str(listaEjemplo.verContenido(i)))

    print("\nExisten " + str(listaEjemplo.getLongitud()) + " elementos en la lista")

main()