Implementa aquí todos los procesos necesarios para la operación de inserción. 
Pueden modificar la extensión del documento para que se ajuste al lenguaje de su elección y comentar estas instrucciones.

class NodoB:
    def __init__(self, t, hoja):
        self.t = t                # Grado mínimo
        self.hoja = hoja          # True si es hoja
        self.claves = []          # Claves del nodo
        self.hijos = []           # Referencias a hijos

    # Inserta una nueva clave en un nodo no lleno
    def insertar_no_lleno(self, k):
        i = len(self.claves) - 1

        if self.hoja:
            # Insertar la clave en el lugar correcto del nodo hoja
            self.claves.append(0)
            while i >= 0 and k < self.claves[i]:
                self.claves[i + 1] = self.claves[i]
                i -= 1
            self.claves[i + 1] = k
        else:
            # Buscar el hijo donde debe ir la clave
            while i >= 0 and k < self.claves[i]:
                i -= 1
            i += 1

            # Si el hijo está lleno, dividirlo
            if len(self.hijos[i].claves) == 2 * self.t - 1:
                self.dividir_hijo(i, self.hijos[i])

                # Después de dividir, decidir a qué hijo bajar
                if k > self.claves[i]:
                    i += 1
            self.hijos[i].insertar_no_lleno(k)

    # Divide un hijo lleno en dos nodos y mueve la clave media al nodo padre
    def dividir_hijo(self, i, y):
        t = self.t
        z = NodoB(t, y.hoja)
        clave_media = y.claves[t - 1]

        # Mitad derecha y mitad izquierda
        z.claves = y.claves[t:]         # Claves mayores
        y.claves = y.claves[:t - 1]     # Claves menores

        if not y.hoja:
            z.hijos = y.hijos[t:]
            y.hijos = y.hijos[:t]

        # Insertar el nuevo hijo y la clave media en el padre
        self.hijos.insert(i + 1, z)
        self.claves.insert(i, clave_media)


class ArbolB:
    def __init__(self, t):
        self.t = t
        self.raiz = NodoB(t, True)

    # Inserta una nueva clave en el árbol B
    def insertar(self, k):
        raiz = self.raiz
        if len(raiz.claves) == 2 * self.t - 1:
            nueva_raiz = NodoB(self.t, False)
            nueva_raiz.hijos.append(raiz)
            nueva_raiz.dividir_hijo(0, raiz)
            i = 0
            if k > nueva_raiz.claves[0]:
                i += 1
            nueva_raiz.hijos[i].insertar_no_lleno(k)
            self.raiz = nueva_raiz
        else:
            raiz.insertar_no_lleno(k)


# Ejemplo de uso
if __name__ == "__main__":
    t = 3  # Grado mínimo
    arbol = ArbolB(t)

    claves = [10, 20, 5, 6, 12, 30, 7, 17]
    for c in claves:
        print(f"Insertando {c}...")
        arbol.insertar(c)

    print("\nÁrbol resultante:")
    nodos = [arbol.raiz]
    nivel = 0
    while nodos:
        print(f"Nivel {nivel}: ", [n.claves for n in nodos])
        nuevos = []
        for n in nodos:
            if not n.hoja:
                nuevos.extend(n.hijos)
        nodos = nuevos
        nivel += 1
