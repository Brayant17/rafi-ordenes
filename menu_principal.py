# menu_principal.py
from datos import MENU_COMIDAS, MENU_BEBIDAS
from pedidos import (agregar_orden, obtener_ordenes, calcular_total,
                     buscar_orden_lineal, buscar_orden_hash,
                     ordenar_ordenes_por_total)
from utils import separador


def menu_principal():
    while True:
        print("1 - Tomar Orden")
        print("2 - Ver Órdenes")
        print("3 - Ganancias del día")
        print("4 - Buscar Orden por ID")
        print("5 - Ver Órdenes Ordenadas por Total")
        print("6 - Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            tomar_orden()
        elif opcion == "2":
            mostrar_ordenes(obtener_ordenes())
        elif opcion == "3":
            print(separador("Ganancias"))
            print(f"Ganancias del día: ${calcular_total()}")
        elif opcion == "4":
            buscar_orden()
        elif opcion == "5":
            print(separador("Ordenadas por Total"))
            mostrar_ordenes(ordenar_ordenes_por_total())
        elif opcion == "6":
            break
        else:
            print("Opción inválida")


def tomar_orden():
    productos = {**MENU_COMIDAS, **MENU_BEBIDAS}
    orden_items = []

    while True:
        print("Seleccione un producto:")
        for clave, valor in productos.items():
            print(f"{clave} - {valor[0]} (${valor[1]})")

        opcion = input("Número del producto: ").strip()

        if opcion in productos:
            nombre, precio = productos[opcion]
            orden_items.append({"producto": nombre, "precio": precio})
            print(f"Agregaste: {nombre} (${precio})")
        else:
            print("Opción inválida")
            continue

        if input("¿Desea agregar otro producto? (s/n): ").lower() != "s":
            break

    if orden_items:
        agregar_orden(orden_items)
        total_orden = sum(item["precio"] for item in orden_items)
        print(f"Orden agregada. Total de la orden: ${total_orden}")


def mostrar_ordenes(ordenes):
    if not ordenes:
        print("No hay órdenes registradas")
        return

    for orden in ordenes:
        print(separador())
        print(f"Orden #{orden['id']}: ")
        for item in orden["productos"]:
            print(f"  - {item['producto']} - ${item['precio']}")
        print(f"  Total: ${orden['total']}")
        print(separador())


def buscar_orden():
    try:
        id_buscado = int(input("Ingresa el ID de la orden: ").strip())
    except ValueError:
        print("ID inválido")
        return

    # Búsqueda lineal (O(n)) — para demostrar el algoritmo
    orden = buscar_orden_lineal(id_buscado)

    # Alternativa O(1) con tabla hash:
    # orden = buscar_orden_hash(id_buscado)

    if orden:
        print(separador("Orden encontrada"))
        print(f"Orden #{orden['id']}:")
        for item in orden["productos"]:
            print(f"  - {item['producto']} - ${item['precio']}")
        print(f"  Total: ${orden['total']}")
    else:
        print(f"No se encontró ninguna orden con ID {id_buscado}")