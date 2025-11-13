Implementa aquí la operación de búsqueda. 
Pueden modificar la extensión del documento para que se ajuste al lenguaje de su elección y comentar estas instrucciones.

class NodoB:
    def __init__(self, t, hoja):
        self.t = t                # Grado mínimo del árbol
        self.hoja = hoja          # True si es un nodo hoja
        self.claves = []          # Lista de claves
        self.hijos = []           # Lista de referencias a hijos

    def buscar(self, k):
        # Encuentra el índice de la primera clave mayor o igual a k
        i = 0
        while i < len(self.claves) and k > self.claves[i]:
            i += 1

        # Si encuentra la clave en este nodo, retorna el nodo
        if i < len(self.claves) and self.claves[i] == k:
            return self

        # Si es hoja, la clave no está en el árbol
        if self.hoja:
            return None

        # Si no es hoja, busca en el hijo correspondiente
        return self.hijos[i].buscar(k)


class ArbolB:
    def __init__(self, t):
        self.t = t
        self.raiz = NodoB(t, True)

    def buscar(self, k):
        if self.raiz is None:
            return None
        else:
            return self.raiz.buscar(k)


#Ejemplo de uso


if __name__ == "__main__":
    t = 3
    arbol = ArbolB(t)

    #Raíz
    raiz = NodoB(t, False)
    raiz.claves = [20, 50]

    # Nivel 1 - hijos
    hijo_izq = NodoB(t, True)
    hijo_izq.claves = [5, 10, 15]

    hijo_centro = NodoB(t, True)
    hijo_centro.claves = [25, 35, 45]

    hijo_der = NodoB(t, True)
    hijo_der.claves = [55, 65, 75, 85]

    # Conectar los hijos a la raíz
    raiz.hijos = [hijo_izq, hijo_centro, hijo_der]
    arbol.raiz = raiz

    # PRUEBAS DE BÚSQUEDA
    claves_a_buscar = [10, 25, 65, 30, 90]

    for clave in claves_a_buscar:
        print(f"\n=== BÚSQUEDA DE {clave} ===")
        resultado = arbol.buscar(clave)
        if resultado:
            print(f"Resultado: clave {clave} encontrada en nodo {resultado.claves}\n")
        else:
            print(f"Resultado: clave {clave} no encontrada\n")
