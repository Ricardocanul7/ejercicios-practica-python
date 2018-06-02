# Ejercicio: Crear una clase con los parametros basicos de una lista y el funcionamiento de la misma
class Lista:
    class Nodo:
        def __init__(self):
            pass

        #def __init__(self, contenido, siguiente):
        #    self.contenido = contenido
        #    self.siguiente = siguiente

        def setObjecto(self, contenido):
            self.contenido = contenido

        def setSiguiente(self, siguiente):
            self.siguiente = siguiente

        def getContenido(self):
            return self.contenido

        def getSiguiente(self):
            return self.siguiente

    nodoInicial = Nodo()
    longitud = 0

    def __init__(self):
        pass

    def agregar(self, objeto):
        if self.longitud == 0:
            self.nodoInicial.setObjecto(objeto)
        pass

    def eliminarPorIndice(self, indice):
        pass

    def objeto(self, indice):
        pass

    def logintud(self):
        return self.logintud


def main():
    lista = Lista()
    lista.agregar("Hola ")
    lista.agregar("Mundo!!!")

    print(lista.objeto(0) + lista.objeto(1))

main()