# arboles.py

# ─────────────────────────────────────────────
#  ÁRBOL N-ARIO DE CATEGORÍAS DEL MENÚ
# ─────────────────────────────────────────────

class NodoCategoria:
    """Nodo de un árbol n-ario para organizar el menú por categorías."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []        # Lista de NodoCategoria
        self.productos = []    # Lista de (nombre_producto, precio)

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)
        return nodo_hijo

    def agregar_producto(self, nombre, precio):
        self.productos.append((nombre, precio))


class ArbolMenu:
    """
    Árbol n-ario que organiza el menú en una jerarquía de categorías.

    Estructura:
        Menú
        ├── Comidas
        │   ├── Plato Principal  →  [Hamburguesa, Pizza, ...]
        │   └── Ensaladas        →  [Ensalada, ...]
        └── Bebidas
            ├── Agua             →  [Agua 600ml, ...]
            └── Refrescos        →  [Refresco, ...]
    """

    def __init__(self):
        self.raiz = NodoCategoria("Menú")
        self._construir_arbol()

    def _construir_arbol(self):
        from datos import MENU_COMIDAS, MENU_BEBIDAS

        # ── Rama Comidas ──────────────────────────────
        comidas = NodoCategoria("Comidas")
        self.raiz.agregar_hijo(comidas)

        platos_principales = NodoCategoria("Platos Principales")
        ensaladas = NodoCategoria("Ensaladas")
        comidas.agregar_hijo(platos_principales)
        comidas.agregar_hijo(ensaladas)

        # Clasificamos los productos de MENU_COMIDAS manualmente
        COMIDAS_CLASIFICADAS = {
            "1": "principales",   # Hamburguesa
            "2": "principales",   # Pizza
            "3": "ensaladas",     # Ensalada
            "4": "principales",   # Tacos
            "5": "principales",   # Rollo de Sushi
            "6": "principales",   # Enchiladas Suizas
        }
        for clave, (nombre, precio) in MENU_COMIDAS.items():
            if COMIDAS_CLASIFICADAS.get(clave) == "principales":
                platos_principales.agregar_producto(nombre, precio)
            else:
                ensaladas.agregar_producto(nombre, precio)

        # ── Rama Bebidas ──────────────────────────────
        bebidas = NodoCategoria("Bebidas")
        self.raiz.agregar_hijo(bebidas)

        aguas = NodoCategoria("Aguas")
        refrescos = NodoCategoria("Refrescos")
        bebidas.agregar_hijo(aguas)
        bebidas.agregar_hijo(refrescos)

        BEBIDAS_CLASIFICADAS = {
            "7": "aguas",
            "8": "aguas",
            "9": "aguas",
            "10": "refrescos",
        }
        for clave, (nombre, precio) in MENU_BEBIDAS.items():
            if BEBIDAS_CLASIFICADAS.get(clave) == "aguas":
                aguas.agregar_producto(nombre, precio)
            else:
                refrescos.agregar_producto(nombre, precio)

    # ── Recorrido DFS (preorden) ───────────────────────────────────────────
    def mostrar(self, nodo=None, nivel=0):
        """Imprime el árbol con indentación jerárquica (DFS preorden)."""
        if nodo is None:
            nodo = self.raiz

        prefijo = "  " * nivel
        print(f"{prefijo}📂 {nodo.nombre}")

        for nombre, precio in nodo.productos:
            print(f"{prefijo}  └─ {nombre} (${precio})")

        for hijo in nodo.hijos:
            self.mostrar(hijo, nivel + 1)

    # ── Búsqueda por nombre de categoría (BFS) ────────────────────────────
    def buscar_categoria(self, nombre_categoria):
        """Busca un nodo por nombre usando BFS. Retorna el nodo o None."""
        from collections import deque
        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            if nodo.nombre.lower() == nombre_categoria.lower():
                return nodo
            for hijo in nodo.hijos:
                cola.append(hijo)
        return None

    def listar_productos_categoria(self, nombre_categoria):
        """Retorna todos los productos de una categoría (y sus subcategorías)."""
        nodo = self.buscar_categoria(nombre_categoria)
        if not nodo:
            return []
        resultado = []
        self._recolectar_productos(nodo, resultado)
        return resultado

    def _recolectar_productos(self, nodo, resultado):
        resultado.extend(nodo.productos)
        for hijo in nodo.hijos:
            self._recolectar_productos(hijo, resultado)


# ─────────────────────────────────────────────
#  BST DE ÓRDENES POR TOTAL
# ─────────────────────────────────────────────

class NodoBST:
    """Nodo de un Árbol Binario de Búsqueda (BST) indexado por total de orden."""

    def __init__(self, orden):
        self.total = orden["total"]
        self.ordenes = [orden]   # Puede haber varias órdenes con el mismo total
        self.izquierda = None
        self.derecha = None


class BSTOrdenes:
    """
    Árbol Binario de Búsqueda (BST) que indexa órdenes por su total.

    Permite:
      - Insertar una orden en O(log n) promedio
      - Búsqueda de órdenes por total exacto en O(log n)
      - Recorrido inorden → órdenes de menor a mayor total en O(n)
      - Búsqueda de órdenes en un rango de precios en O(log n + k)
    """

    def __init__(self):
        self.raiz = None

    # ── Inserción ─────────────────────────────────────────────────────────
    def insertar(self, orden):
        self.raiz = self._insertar(self.raiz, orden)

    def _insertar(self, nodo, orden):
        if nodo is None:
            return NodoBST(orden)
        if orden["total"] < nodo.total:
            nodo.izquierda = self._insertar(nodo.izquierda, orden)
        elif orden["total"] > nodo.total:
            nodo.derecha = self._insertar(nodo.derecha, orden)
        else:
            # Mismo total → guardamos ambas órdenes en el mismo nodo
            nodo.ordenes.append(orden)
        return nodo

    # ── Búsqueda exacta ───────────────────────────────────────────────────
    def buscar_por_total(self, total):
        """Retorna lista de órdenes con ese total exacto, o [] si no hay."""
        nodo = self._buscar(self.raiz, total)
        return nodo.ordenes if nodo else []

    def _buscar(self, nodo, total):
        if nodo is None or nodo.total == total:
            return nodo
        if total < nodo.total:
            return self._buscar(nodo.izquierda, total)
        return self._buscar(nodo.derecha, total)

    # ── Recorrido inorden (menor → mayor) ─────────────────────────────────
    def inorden(self):
        """Retorna todas las órdenes ordenadas de menor a mayor total."""
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo is None:
            return
        self._inorden(nodo.izquierda, resultado)
        resultado.extend(nodo.ordenes)
        self._inorden(nodo.derecha, resultado)

    # ── Búsqueda por rango ────────────────────────────────────────────────
    def buscar_rango(self, minimo, maximo):
        """Retorna órdenes cuyo total esté en [minimo, maximo]."""
        resultado = []
        self._buscar_rango(self.raiz, minimo, maximo, resultado)
        return resultado

    def _buscar_rango(self, nodo, minimo, maximo, resultado):
        if nodo is None:
            return
        if minimo < nodo.total:
            self._buscar_rango(nodo.izquierda, minimo, maximo, resultado)
        if minimo <= nodo.total <= maximo:
            resultado.extend(nodo.ordenes)
        if maximo > nodo.total:
            self._buscar_rango(nodo.derecha, minimo, maximo, resultado)

    def esta_vacio(self):
        return self.raiz is None


# ─────────────────────────────────────────────
#  INSTANCIAS GLOBALES (se importan donde se necesiten)
# ─────────────────────────────────────────────
arbol_menu = ArbolMenu()
bst_ordenes = BSTOrdenes()