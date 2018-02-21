class Nodo:
 
    def __init__(self,arbol,dato):
        # crea un nodo
        self.izq = None
        self.der = None
        self.dato = dato
        
    def preorden(self,arbol):
        print(arbol.dato,end=' ')
        if arbol.izq!=None:
            self.preoIzq(arbol)
        if arbol.der!=None:
            self.preoDer(arbol)

    def preoIzq(self,arbol):
        self.preorden(arbol.izq)

    def preoDer(self,arbol):
        self.preorden(arbol.der)

    def inorden(self,arbol):
        if arbol.izq!=None:
            self.inorIzq(arbol)
        print(arbol.dato,end=' ')
        if arbol.der!=None:
            self.inorDer(arbol)

    def inorIzq(self,arbol):
        self.inorden(arbol.izq)

    def inorDer(self,arbol):
        self.inorden(arbol.der)
