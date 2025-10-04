class NodoCategoria:
    def __init__(self, id_categoria, nombre):
        self.id = id_categoria
        self.nombre = nombre
        self.izquierdo = None  # Cambié 'iquierdo' por 'izquierdo'
        self.derecho = None

def insertar(raiz, id_categoria, nombre):
    if raiz is None:
        return NodoCategoria(id_categoria, nombre)
    if id_categoria < raiz.id:
        raiz.izquierdo = insertar(raiz.izquierdo, id_categoria, nombre)  # Accedo a 'izquierdo' correctamente
    elif id_categoria > raiz.id:
        raiz.derecho = insertar(raiz.derecho, id_categoria, nombre)  # Accedo a 'derecho' correctamente
    return raiz

def buscar(raiz, id_categoria):
    if raiz is None or raiz.id == id_categoria:
        return raiz
    if id_categoria < raiz.id:
        return buscar(raiz.izquierdo, id_categoria)  # Accedo a 'izquierdo' correctamente
    return buscar(raiz.derecho, id_categoria)  # Accedo a 'derecho' correctamente

def inorder(raiz):
     if raiz:
        inorder(raiz.izquierdo)  # Accedo a 'izquierdo' correctamente
        print(f"ID:{raiz.id}, Categoria: {raiz.nombre}")
        inorder(raiz.derecho)  # Accedo a 'derecho' correctamente

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

print("\nBuscar categoria con ID 60:")
resultado = buscar(raiz, 60)
if resultado:
    print(f"Encontrada: {resultado.nombre}")
else:
    print("Categoria no encontrada")
