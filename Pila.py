# -*- coding: utf-8 -*-
class Cola:
    
    def __init__(self):
        self.items=[]

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        return self.items == []

    
