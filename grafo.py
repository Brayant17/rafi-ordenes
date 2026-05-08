# grafo.py

# ─────────────────────────────────────────────
#  GRAFO DIRIGIDO: FLUJO DE ESTADOS DE ORDEN
# ─────────────────────────────────────────────
#
#  Estados posibles:
#    pendiente ──► en_proceso ──► lista ──► entregada
#                                       └──► cancelada
#    (desde pendiente también se puede cancelar)
#
#  Representación: lista de adyacencia con pesos descriptivos.

class GrafoEstados:
    """
    Grafo dirigido que modela las transiciones válidas entre estados de una orden.

    Nodos   → estados de la orden
    Aristas → transiciones permitidas (con una acción descriptiva)
    """

    def __init__(self):
        # { estado: [(estado_destino, acción)] }
        self._adyacencia = {}
        self._construir_grafo()

    def _construir_grafo(self):
        estados = ["pendiente", "en_proceso", "lista", "entregada", "cancelada"]
        for estado in estados:
            self._adyacencia[estado] = []

        # Definimos las transiciones válidas
        transiciones = [
            ("pendiente",   "en_proceso", "Iniciar preparación"),
            ("pendiente",   "cancelada",  "Cancelar orden"),
            ("en_proceso",  "lista",      "Marcar como lista"),
            ("en_proceso",  "cancelada",  "Cancelar durante preparación"),
            ("lista",       "entregada",  "Entregar al cliente"),
            ("lista",       "cancelada",  "Cancelar antes de entregar"),
        ]

        for origen, destino, accion in transiciones:
            self._adyacencia[origen].append((destino, accion))

    # ── Consultas del grafo ───────────────────────────────────────────────

    def transiciones_validas(self, estado_actual):
        """Retorna lista de (estado_destino, acción) desde el estado actual."""
        return self._adyacencia.get(estado_actual, [])

    def transicion_es_valida(self, estado_actual, estado_destino):
        """Verifica si la transición estado_actual → estado_destino existe."""
        return any(dest == estado_destino
                   for dest, _ in self._adyacencia.get(estado_actual, []))

    def todos_los_estados(self):
        return list(self._adyacencia.keys())

    # ── Búsqueda de caminos (BFS) ─────────────────────────────────────────

    def hay_camino(self, origen, destino):
        """BFS: verifica si existe algún camino de origen a destino."""
        if origen == destino:
            return True
        visitados = set()
        cola = [origen]
        while cola:
            actual = cola.pop(0)
            if actual in visitados:
                continue
            visitados.add(actual)
            for vecino, _ in self._adyacencia.get(actual, []):
                if vecino == destino:
                    return True
                cola.append(vecino)
        return False

    def camino_mas_corto(self, origen, destino):
        """BFS: retorna la lista de estados del camino más corto, o [] si no existe."""
        if origen == destino:
            return [origen]
        visitados = set()
        cola = [(origen, [origen])]
        while cola:
            actual, camino = cola.pop(0)
            if actual in visitados:
                continue
            visitados.add(actual)
            for vecino, _ in self._adyacencia.get(actual, []):
                nuevo_camino = camino + [vecino]
                if vecino == destino:
                    return nuevo_camino
                cola.append((vecino, nuevo_camino))
        return []

    # ── Visualización del grafo ───────────────────────────────────────────

    def mostrar_grafo(self):
        print("Grafo de estados de órdenes:")
        for estado, vecinos in self._adyacencia.items():
            if vecinos:
                for destino, accion in vecinos:
                    print(f"  [{estado}]  ──({accion})──►  [{destino}]")
            else:
                print(f"  [{estado}]  (estado terminal)")


# ─────────────────────────────────────────────
#  MANEJADOR DE ESTADO POR ORDEN
# ─────────────────────────────────────────────

grafo_estados = GrafoEstados()

# { id_orden: estado_actual }
_estado_ordenes = {}

ESTADO_INICIAL = "pendiente"


def inicializar_estado_orden(id_orden):
    """Registra una nueva orden con estado 'pendiente'."""
    _estado_ordenes[id_orden] = ESTADO_INICIAL


def obtener_estado_orden(id_orden):
    """Retorna el estado actual de la orden, o None si no existe."""
    return _estado_ordenes.get(id_orden)


def avanzar_estado(id_orden, nuevo_estado):
    """
    Intenta hacer la transición del estado actual al nuevo_estado.
    Retorna (True, mensaje) si es válida, (False, mensaje) si no lo es.
    """
    estado_actual = _estado_ordenes.get(id_orden)
    if estado_actual is None:
        return False, f"La orden #{id_orden} no existe."

    if grafo_estados.transicion_es_valida(estado_actual, nuevo_estado):
        _estado_ordenes[id_orden] = nuevo_estado
        return True, f"Orden #{id_orden}: {estado_actual} → {nuevo_estado}"
    else:
        validas = [d for d, _ in grafo_estados.transiciones_validas(estado_actual)]
        return False, (
            f"Transición inválida: [{estado_actual}] → [{nuevo_estado}].\n"
            f"  Transiciones permitidas desde '{estado_actual}': {validas}"
        )


def obtener_todas_las_ordenes_con_estado():
    return dict(_estado_ordenes)