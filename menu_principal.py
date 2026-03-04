from datos import MENU_COMIDAS, MENU_BEBIDAS
from pedidos import agregar_orden, obtener_ordenes, calcular_total

def menu_principal():
    while True:
        print("1 - Tomar Orden")
        print("2 - Ver Ordenes")
        print("3 - Ganancias del día")
        print("4 - Salir")

        opcion = input()

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
    while True:

        print("Seleccione comida:")
        for clave, valor in MENU_COMIDAS.items():
            print(f"{clave} - {valor[0]} (${valor[1]})")

        opcion = input()

        if opcion in MENU_COMIDAS:
            nombre, precio = MENU_COMIDAS[opcion]
            agregar_orden(nombre, precio)
            print("Producto agregado")
        else:
            print("Opción inválida")
            continue

        print("¿Desea agregar otro producto? (s/n)")
        if input().lower() != "s":
            break


def mostrar_ordenes():
    ordenes = obtener_ordenes()

    if not ordenes:
        print("No hay órdenes registradas")
        return

    for orden in ordenes:
        print(f"{orden['producto']} - ${orden['precio']}")
