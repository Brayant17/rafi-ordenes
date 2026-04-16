from datos import ordenes

def agregar_orden(productos):
    total = sum(item["precio"] for item in productos)
    orden = {
        "id": len(ordenes) + 1,
        "productos": productos,
        "total": total
    }
    ordenes.append(orden)

def obtener_ordenes():
    return ordenes.copy()

def calcular_total():
    return sum(orden["total"] for orden in ordenes)
