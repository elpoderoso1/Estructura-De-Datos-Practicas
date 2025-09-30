class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

raiz = Nodo(1)
raiz.izq = Nodo(2)
raiz.der = Nodo(3)
raiz.izq.izq = Nodo(4)
raiz.izq.der = Nodo(5)
raiz.der.izq = Nodo(6)
raiz.der.der = Nodo(7)
raiz.izq.der.izq = Nodo(8)

print("Raiz: ", raiz.valor)
print("Raiz: ", raiz.izq)
print("Raiz: ", raiz.der.izq)
print("Raiz: ", raiz.izq.der.izq)
print("Raiz: ")