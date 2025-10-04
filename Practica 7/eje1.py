class NodoCategoria:
    def __init__(self, id_categoria, nombre):
        self.id = id_categoria
        self.nombre = nombre
        self.iquierdo = None
        self.derecho = None

def insertar(raiz, id_categoria, nombre):
    if raiz is None:
        return NodoCategoria(id_categoria, nombre)
    if id_categoria < raiz.id:
        raiz.izquierdo = insertar(raiz.izquierdo, id_categoria, nombre)
    elif id_categoria > raiz.id:
                raiz.derecho = insertar (raiz.derecho, id_categoria, nombre)
    return raiz

def buscar(raiz, id_categoria):
    if raiz is None or raiz.id == id_categoria:
        return raiz
    if id_categoria < raiz.id:
        return buscar(raiz.izquierdo, id_categoria)
    return buscar(raiz.derecho, id_categoria)

def inorder(raiz):
     if raiz:
        inorder(raiz.izquierdo)
        print(f"ID:{raiz.id}, Categoria: {raiz.nombre}")
        inorder(raiz.derecho)

raiz = None
categoria = [
    (50, "Biblioteca"),
    (30, "Literatura"),
    (20, "Novela"),
    (40, "Poesia"),
    (70, "Ciencia"),
    (60, "Matematicas"),
    (80, "Historia")
]

for id_categoria, nombre in categoria:
    raiz = insertar(raiz, id_categoria, nombre)

print("Listado de Categorias (Inorder):")
inorder(raiz)

print("\nBuscar categorias con ID 60:")
resultado = buscar(raiz, 60)
if resultado:
    print(f"Encontrada: {resultado.nombre}")
else:
    print("Categoria no encontrada")