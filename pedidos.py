from datos import ordenes

def agregar_orden(producto, precio):
    orden = {
        "producto": producto,
        "precio": precio
    }
    ordenes.append(orden)

def obtener_ordenes():
    return ordenes

def calcular_total():
    total = 0
    for orden in ordenes:
        total += orden["precio"]
    return total
