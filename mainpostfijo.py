# -*- coding: utf-8 -*-
from pila import Pila
from arbol import Nodo
class prueba:
    arbolbase = Pila()
    arbolbase.apilar(5)
    arbolbase.apilar(1)
    arbolbase.apilar(63)
    arbolbase.apilar(2)

    print (arbolbase.desapilar())
    print (arbolbase.desapilar())
    print (arbolbase.desapilar())
    print (arbolbase.desapilar())
    
