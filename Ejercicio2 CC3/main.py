# -*- coding: utf-8 -*-
from pila import Pila
from cola import Cola

"""Se representa una lista de generos de peliculas en una pila"""

class prueba():
    def __init__(self, nombre, genero):
        """ Crea una cola vacía. """
        self.nombre=nombre
        self.genero=genero

#Se definen los objetos pelicula

pelicula1 = prueba("transformers","accion")
pelicula2 = prueba("rapidos y furuiosos","accion")
pelicula3 = prueba("busqueda implacable","accion")
pelicula4 = prueba("rec","terror")
pelicula5 = prueba("el rito","terror")
pelicula6 = prueba("anabelle","terror")
pelicula7 = prueba("matrix","ficcion")
pelicula8 = prueba("guerra mundial z","ficcion")
pelicula9 = prueba("avatar","ficcion")
pelicula10 = prueba("monsters inc.","animadas")
pelicula11 = prueba("toy story","animadas")
pelicula12 = prueba("cars","animadas")
pelicula13 = prueba("la pelota de letras","comedia")
pelicula14 = prueba("me pido la ventana","comedia")
pelicula15 = prueba("infraganti","comedia")
pelicula16 = prueba("","")

#Se crea la pila que contiene todas las peliculas

peliculas = Pila()

#Usamos el método de apilar, para agregar peliculas

peliculas.apilar(pelicula1)
peliculas.apilar(pelicula2)
peliculas.apilar(pelicula3)
peliculas.apilar(pelicula4)
peliculas.apilar(pelicula5)
peliculas.apilar(pelicula6)
peliculas.apilar(pelicula7)
peliculas.apilar(pelicula8)
peliculas.apilar(pelicula9)
peliculas.apilar(pelicula10)
peliculas.apilar(pelicula11)
peliculas.apilar(pelicula12)
peliculas.apilar(pelicula13)
peliculas.apilar(pelicula14)
peliculas.apilar(pelicula15)

#Se pide la entrada del genero que se desea obtener

print "Escriba el genero deseado para buscar peliculas del mismo tipo"
generoDeseado = raw_input()

#Se crea la cola de peliculas del genero seleccionado

seleccionadas = Cola()

while (peliculas.es_vacia() == False):
    pelicula16 = peliculas.desapilar()
    if (pelicula16.genero==generoDeseado):
        seleccionadas.encolar(pelicula16)

#Se le da a escoger al usuario la pelicula

escogida = False
contador = 0
while(seleccionadas.es_vacia() == False and escogida == False):
    contador=+contador+1
    print "La pelicula #", contador, "del genero seleccionado es: ", seleccionadas.desencolar().nombre
    print "¿Esta es la deseada?, responda True si esta es, por el contrario responda False"
    escogida = input()
    if(seleccionadas.es_vacia()==True and escogida==False):
        print "No existen mas peliculas de este genero, lo sentimos"
    elif(escogida == True):
        print "Te felicitamos por encontrar el titulo que buscabas"
