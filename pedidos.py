# pedidos.py
from datos import ordenes

# --- Tabla Hash explícita: índice de órdenes por ID ---
_indice_ordenes = {}  # { id: orden }


def agregar_orden(productos):
    total = sum(item["precio"] for item in productos)
    orden = {
        "id": len(ordenes) + 1,
        "productos": productos,
        "total": total
    }
    ordenes.append(orden)
    _indice_ordenes[orden["id"]] = orden  # Inserción en tabla hash O(1)


def obtener_ordenes():
    return ordenes.copy()


def calcular_total():
    return sum(orden["total"] for orden in ordenes)


# --- Búsqueda lineal: busca orden por ID recorriendo la lista ---
def buscar_orden_lineal(id_buscado):
    for orden in ordenes:
        if orden["id"] == id_buscado:
            return orden
    return None


# --- Búsqueda por tabla hash: O(1) ---
def buscar_orden_hash(id_buscado):
    return _indice_ordenes.get(id_buscado, None)


# --- Bubble Sort: ordena órdenes de menor a mayor total ---
def ordenar_ordenes_por_total():
    lista = ordenes.copy()
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j]["total"] > lista[j + 1]["total"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista