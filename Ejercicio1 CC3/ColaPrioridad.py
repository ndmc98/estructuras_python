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
