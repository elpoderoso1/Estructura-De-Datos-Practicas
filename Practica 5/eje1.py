class Cola:
    def __init__(self):
        self.elementos = []
    def esta_vacia(self):
        return len(self.elementos) == 0
    def encolar(self, item):
        self.elementos.append(item)
    def desencolar(self):
        return self.elementos.pop(0) if not self.esta_vacia() else "Cola vacias"
    
cola_estudiante = Cola()
cola_estudiante.encolar("Sofia")
cola_estudiante.encolar("Mario")
cola_estudiante.encolar("Lucia")

print("Entrega primero:", cola_estudiante.desencolar())
print("Queda em fila:", cola_estudiante.elementos)