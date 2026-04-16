from datos import MENU_COMIDAS, MENU_BEBIDAS
from pedidos import agregar_orden, obtener_ordenes, calcular_total

def menu_principal():
    while True:
        print("1 - Tomar Orden")
        print("2 - Ver Órdenes")
        print("3 - Ganancias del día")
        print("4 - Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            tomar_orden()
        elif opcion == "2":
            mostrar_ordenes()
        elif opcion == "3":
            print(f"Ganancias del día: ${calcular_total()}")
        elif opcion == "4":
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


def mostrar_ordenes():
    ordenes = obtener_ordenes()

    if not ordenes:
        print("No hay órdenes registradas")
        return

    for orden in ordenes:
        print(f"Orden #{orden['id']}: ")
        for item in orden["productos"]:
            print(f"  - {item['producto']} - ${item['precio']}")
        print(f"  Total: ${orden['total']}")
