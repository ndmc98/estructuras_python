# -*- coding: utf-8 -*-
from pila import Pila
from cola import Cola
"""Se representa una lista de generos de peliculas en una pila"""
class prueba:
    ficcion = Pila()
    accion = Pila()
    drama = Pila()
    amor = Pila()
    terror = Pila()
    genero = Cola()
    ficcion.apilar("transformers")
    ficcion.apilar("guerra mundial z")
    ficcion.apilar("hallo")
    ficcion.apilar("avatar")
    genero.encolar(ficcion)
    genero.encolar(accion)
    genero.encolar(drama)
    genero.encolar(amor)
    genero.encolar(terror)
    
    print genero.desencolar().desapilar()
