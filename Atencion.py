# -*- coding: cp1252 -*-
class ColaPrioridad:
    def __init__(self):
        self.items = []

    def encolar(self, x):
        self.items.append(x)

    def primero(self):
        if len(self.items) == 0:
            return None
        max = self.items[0].prioridad
        for element in self.items:
            if element > max:
                max = element
        return max

    def des_prim(self):
        return self.items.pop(0)

    def desencolar(self):
        if len(self.items) == 0:
            return None
        ind = 0
        for i in range(len(self.items)):
            if self.items[i].prioridad >= self.items[ind].prioridad:
                ind = i
        aux = self.items[ind]
        del self.items[ind]
        return aux

    def tamano(self):
        return len(self.items)

    def es_vacia(self):
        return len(self.items) == 0

class Atencion:

    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

dicP = {'dolor leve' : 1, 'dolor medio' : 2, 'dolor intenso' : 3, 'accidente leve' : 4, 'accidente grave' : 5, 'atencion inmediata' :  6}
colaP = ColaPrioridad()

while True:
    try:
        opc = raw_input("1: Añadir. 2: Atender por Prioridad 3. Atender por Llegada 4. Siguiente en cola 5. En espera -> ")
        if opc == '1':
            paciente = Atencion(raw_input("Nombre paciente: "), raw_input("Gravedad dolencia: "))
            valor = dicP.get(paciente.prioridad)
            paciente.prioridad = valor
            colaP.encolar(paciente)
            print ('Se añadio al usario a la linea de espera')
    
        elif opc == '2':
            print (colaP.desencolar().nombre)
            print ('Se atendio')

        elif opc == '3':
            print (colaP.des_prim().nombre)
            print ('Se atendio')

        elif opc == '4':
            print (colaP.primero().nombre)

        elif opc == '5':
            print colaP.tamano(), "paciente(s) en espera"

    except:
        print ("...Intente añadiendo para consultar...")
