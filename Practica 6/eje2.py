class recorrido:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def preorden(nodo): 
    if nodo:
        print(nodo.valor, end=" ")
        preorden(nodo.izq)
        preorden(nodo.der)

def inordern(nodo):
    if nodo:
        inordern(nodo.izq)
        print(nodo.valor, end=" ")
        inordern(nodo.der)

def postorden(nodo):
    if nodo: 
        postorden(nodo.izq)
        postorden(nodo.izq)
        print(nodo.valor, emd=" ")

#Creamos el arbol
raiz = recorrido("A")
raiz.izq = recorrido("B")
raiz.der = recorrido("C")
raiz.izq.izq = recorrido("D")
raiz.izq.der = recorrido("E")
raiz.der.izq = recorrido("F")
raiz.der.der = recorrido("G")

preorden("Recorrido Preorden: ")
preorden(raiz)
