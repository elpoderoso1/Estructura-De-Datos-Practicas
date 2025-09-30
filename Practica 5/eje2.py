class Cola:
    def __init__(self):
        self.elementos = []
    def esta_vacia(self):
        return len(self.elementos) == 0
    def encolar(self, item):
        self.elementos.append(item)
    def desencolar(self):
        return self.elementos.pop(0) if not self.esta_vacia() else "Cola vacias"
    
cola_Hospital = Cola()
cola_Hospital.encolar("Paciente Juan")
cola_Hospital.encolar("Paciente Marta")
cola_Hospital.encolar("Paciente Pablo")

print("Entrega primero:", cola_Hospital.desencolar())
print("Queda em fila:", cola_Hospital.elementos)