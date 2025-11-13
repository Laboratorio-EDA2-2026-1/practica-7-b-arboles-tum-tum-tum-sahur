Implementa aquí todos los procesos necesarios para la operación de eliminación. 
Pueden modificar la extensión del documento para que se ajuste al lenguaje de su elección y comentar estas instrucciones.

class NodoB:
    def __init__(self, t, hoja):
        self.t = t                # Grado mínimo
        self.hoja = hoja          # True si es hoja
        self.claves = []          # Claves del nodo
        self.hijos = []           # Referencias a hijos

    # Eliminación de una clave
    def eliminar(self, k):
        i = 0
        while i < len(self.claves) and k > self.claves[i]:
            i += 1

        # Caso 1: la clave está en este nodo
        if i < len(self.claves) and self.claves[i] == k:
            if self.hoja:
                # Caso 1A: la clave está en un nodo hoja
                print(f"Eliminando {k} de hoja {self.claves}")
                self.claves.pop(i)
            else:
                # Caso 1B: la clave está en un nodo interno
                self._eliminar_interno(i)
        else:
            # Caso 2: la clave no está en este nodo
            if self.hoja:
                print(f"Clave {k} no encontrada (nodo hoja {self.claves})")
                return

            # Verifica que el hijo tenga al menos t claves antes de bajar
            if len(self.hijos[i].claves) < self.t:
                self._llenar(i)

            # Puede cambiar el índice si hubo fusión
            if i > len(self.claves):
                self.hijos[i - 1].eliminar(k)
            else:
                self.hijos[i].eliminar(k)

    # Eliminar clave de un nodo interno
    def _eliminar_interno(self, i):
        k = self.claves[i]
        if len(self.hijos[i].claves) >= self.t:
            predecesor = self._obtener_predecesor(i)
            self.claves[i] = predecesor
            self.hijos[i].eliminar(predecesor)
        elif len(self.hijos[i + 1].claves) >= self.t:
            sucesor = self._obtener_sucesor(i)
            self.claves[i] = sucesor
            self.hijos[i + 1].eliminar(sucesor)
        else:
            self._fusionar(i)
            self.hijos[i].eliminar(k)

    # Obtener predecesor (mayor en hijo izquierdo)
    def _obtener_predecesor(self, i):
        actual = self.hijos[i]
        while not actual.hoja:
            actual = actual.hijos[-1]
        return actual.claves[-1]

    # Obtener sucesor (menor en hijo derecho)
    def _obtener_sucesor(self, i):
        actual = self.hijos[i + 1]
        while not actual.hoja:
            actual = actual.hijos[0]
        return actual.claves[0]

    # Llenar un hijo si tiene menos de t-1 claves
    def _llenar(self, i):
        if i != 0 and len(self.hijos[i - 1].claves) >= self.t:
            self._tomar_de_anterior(i)
        elif i != len(self.claves) and len(self.hijos[i + 1].claves) >= self.t:
            self._tomar_de_siguiente(i)
        else:
            if i != len(self.claves):
                self._fusionar(i)
            else:
                self._fusionar(i - 1)

    # Tomar una clave del hijo anterior
    def _tomar_de_anterior(self, i):
        hijo = self.hijos[i]
        hermano = self.hijos[i - 1]

        hijo.claves.insert(0, self.claves[i - 1])
        if not hijo.hoja:
            hijo.hijos.insert(0, hermano.hijos.pop())
        self.claves[i - 1] = hermano.claves.pop()

    # Tomar una clave del hijo siguiente
    def _tomar_de_siguiente(self, i):
        hijo = self.hijos[i]
        hermano = self.hijos[i + 1]

        hijo.claves.append(self.claves[i])
        if not hijo.hoja:
            hijo.hijos.append(hermano.hijos.pop(0))
        self.claves[i] = hermano.claves.pop(0)

    # Fusionar hijo[i] con hijo[i+1]
    def _fusionar(self, i):
        hijo = self.hijos[i]
        hermano = self.hijos[i + 1]
        hijo.claves.append(self.claves.pop(i))
        hijo.claves.extend(hermano.claves)
        if not hijo.hoja:
            hijo.hijos.extend(hermano.hijos)
        self.hijos.pop(i + 1)


class ArbolB:
    def __init__(self, t):
        self.t = t
        self.raiz = NodoB(t, True)

    def eliminar(self, k):
        if not self.raiz:
            print("Árbol vacío")
            return

        self.raiz.eliminar(k)

        # Si la raíz se queda sin claves y tiene hijos
        if len(self.raiz.claves) == 0:
            if not self.raiz.hoja:
                self.raiz = self.raiz.hijos[0]
            else:
                self.raiz = None


# Ejemplo de uso
if __name__ == "__main__":
    t = 3
    arbol = ArbolB(t)

    # Construcción manual (igual que antes)
    raiz = NodoB(t, False)
    raiz.claves = [20, 50]

    hijo1 = NodoB(t, True)
    hijo1.claves = [5, 10, 15]

    hijo2 = NodoB(t, True)
    hijo2.claves = [25, 35, 45]

    hijo3 = NodoB(t, True)
    hijo3.claves = [55, 65, 75, 85]

    raiz.hijos = [hijo1, hijo2, hijo3]
    arbol.raiz = raiz

    # Mostrar árbol antes
    print("Árbol inicial:")
    for h in arbol.raiz.hijos:
        print(" ", h.claves)
    print()

    # Pruebas de eliminación
    claves_a_eliminar = [10, 35, 20, 85, 100]

    for k in claves_a_eliminar:
        print(f"\n=== Eliminando {k} ===")
        arbol.eliminar(k)
        print("Nodo raíz:", arbol.raiz.claves)
        for i, h in enumerate(arbol.raiz.hijos):
            print(f"  Hijo {i}:", h.claves)
        print("===========================")
