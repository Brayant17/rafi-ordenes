# menu_principal.py
from datos import MENU_COMIDAS, MENU_BEBIDAS
from pedidos import (agregar_orden, obtener_ordenes, calcular_total,
                     buscar_orden_lineal, buscar_orden_hash,
                     ordenar_ordenes_por_total,
                     buscar_ordenes_por_total, ordenar_ordenes_bst,
                     buscar_ordenes_rango)
from arboles import arbol_menu
from grafo import (grafo_estados, obtener_estado_orden,
                   avanzar_estado, obtener_todas_las_ordenes_con_estado)
from utils import separador


def menu_principal():
    while True:
        print(separador("MENÚ PRINCIPAL"))
        print("1 - Tomar Orden")
        print("2 - Ver Órdenes")
        print("3 - Ganancias del día")
        print("4 - Buscar Orden por ID")
        print("5 - Ver Órdenes Ordenadas por Total")
        print("--- Árboles ---")
        print("6 - Ver Árbol de Categorías del Menú")
        print("7 - Buscar Órdenes por Total (BST)")
        print("8 - Buscar Órdenes por Rango de Precio (BST)")
        print("--- Grafo ---")
        print("9 - Ver Flujo de Estados de Órdenes")
        print("10 - Avanzar Estado de una Orden")
        print("11 - Ver Estado de una Orden")
        print("0 - Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            tomar_orden()
        elif opcion == "2":
            mostrar_ordenes(obtener_ordenes(), mostrar_estado=True)
        elif opcion == "3":
            print(separador("Ganancias"))
            print(f"Ganancias del día: ${calcular_total()}")
        elif opcion == "4":
            buscar_orden()
        elif opcion == "5":
            print(separador("Ordenadas por Total (Bubble Sort)"))
            mostrar_ordenes(ordenar_ordenes_por_total())
        elif opcion == "6":
            menu_arbol_categorias()
        elif opcion == "7":
            menu_bst_total()
        elif opcion == "8":
            menu_bst_rango()
        elif opcion == "9":
            menu_grafo_estados()
        elif opcion == "10":
            menu_avanzar_estado()
        elif opcion == "11":
            menu_ver_estado()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")


# ─────────────────────────────────────────────
#  FUNCIONES EXISTENTES
# ─────────────────────────────────────────────

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


def mostrar_ordenes(ordenes, mostrar_estado=False):
    if not ordenes:
        print("No hay órdenes registradas")
        return

    for orden in ordenes:
        print(separador())
        print(f"Orden #{orden['id']}: ")
        for item in orden["productos"]:
            print(f"  - {item['producto']} - ${item['precio']}")
        print(f"  Total: ${orden['total']}")
        if mostrar_estado:
            estado = obtener_estado_orden(orden["id"]) or "desconocido"
            print(f"  Estado: [{estado}]")
        print(separador())


def buscar_orden():
    try:
        id_buscado = int(input("Ingresa el ID de la orden: ").strip())
    except ValueError:
        print("ID inválido")
        return

    orden = buscar_orden_lineal(id_buscado)

    if orden:
        print(separador("Orden encontrada"))
        print(f"Orden #{orden['id']}:")
        for item in orden["productos"]:
            print(f"  - {item['producto']} - ${item['precio']}")
        print(f"  Total: ${orden['total']}")
        estado = obtener_estado_orden(orden["id"]) or "desconocido"
        print(f"  Estado: [{estado}]")
    else:
        print(f"No se encontró ninguna orden con ID {id_buscado}")


# ─────────────────────────────────────────────
#  ÁRBOL DE CATEGORÍAS
# ─────────────────────────────────────────────

def menu_arbol_categorias():
    print(separador("Árbol de Categorías del Menú"))
    arbol_menu.mostrar()

    resp = input("\n¿Deseas ver productos de una categoría específica? (s/n): ").lower()
    if resp == "s":
        cat = input("Nombre de categoría (Comidas / Bebidas / Aguas / Refrescos / etc.): ").strip()
        productos = arbol_menu.listar_productos_categoria(cat)
        if productos:
            print(f"\nProductos en '{cat}':")
            for nombre, precio in productos:
                print(f"  - {nombre}: ${precio}")
        else:
            print(f"Categoría '{cat}' no encontrada.")


# ─────────────────────────────────────────────
#  BST DE ÓRDENES
# ─────────────────────────────────────────────

def menu_bst_total():
    print(separador("BST — Buscar por Total Exacto"))
    try:
        total = float(input("Ingresa el total a buscar: $").strip())
    except ValueError:
        print("Valor inválido")
        return

    resultados = buscar_ordenes_por_total(total)
    if resultados:
        print(f"Órdenes con total ${total}:")
        mostrar_ordenes(resultados, mostrar_estado=True)
    else:
        print(f"No se encontraron órdenes con total ${total}")

    print(separador("BST — Todas las Órdenes (inorden, menor → mayor)"))
    todas = ordenar_ordenes_bst()
    mostrar_ordenes(todas)


def menu_bst_rango():
    print(separador("BST — Buscar por Rango de Precio"))
    try:
        minimo = float(input("Total mínimo: $").strip())
        maximo = float(input("Total máximo: $").strip())
    except ValueError:
        print("Valores inválidos")
        return

    resultados = buscar_ordenes_rango(minimo, maximo)
    if resultados:
        print(f"Órdenes entre ${minimo} y ${maximo}:")
        mostrar_ordenes(resultados, mostrar_estado=True)
    else:
        print(f"No se encontraron órdenes en ese rango.")


# ─────────────────────────────────────────────
#  GRAFO DE ESTADOS
# ─────────────────────────────────────────────

def menu_grafo_estados():
    print(separador("Grafo de Estados"))
    grafo_estados.mostrar_grafo()

    print()
    estados_ordenes = obtener_todas_las_ordenes_con_estado()
    if estados_ordenes:
        print("Estado actual de las órdenes:")
        for id_ord, estado in estados_ordenes.items():
            print(f"  Orden #{id_ord}: [{estado}]")
    else:
        print("No hay órdenes registradas aún.")


def menu_avanzar_estado():
    print(separador("Avanzar Estado de Orden"))
    try:
        id_orden = int(input("ID de la orden: ").strip())
    except ValueError:
        print("ID inválido")
        return

    estado_actual = obtener_estado_orden(id_orden)
    if estado_actual is None:
        print(f"Orden #{id_orden} no encontrada.")
        return

    print(f"Estado actual: [{estado_actual}]")
    transiciones = grafo_estados.transiciones_validas(estado_actual)

    if not transiciones:
        print("Esta orden está en un estado terminal, no puede avanzar.")
        return

    print("Transiciones disponibles:")
    for i, (destino, accion) in enumerate(transiciones, 1):
        print(f"  {i} - {accion}  →  [{destino}]")

    try:
        eleccion = int(input("Elige una opción: ").strip()) - 1
        nuevo_estado = transiciones[eleccion][0]
    except (ValueError, IndexError):
        print("Opción inválida")
        return

    exito, mensaje = avanzar_estado(id_orden, nuevo_estado)
    print(mensaje)


def menu_ver_estado():
    print(separador("Ver Estado de Orden"))
    try:
        id_orden = int(input("ID de la orden: ").strip())
    except ValueError:
        print("ID inválido")
        return

    estado = obtener_estado_orden(id_orden)
    if estado is None:
        print(f"Orden #{id_orden} no encontrada.")
        return

    print(f"Orden #{id_orden}: [{estado}]")
    transiciones = grafo_estados.transiciones_validas(estado)
    if transiciones:
        print("Puede avanzar a:")
        for destino, accion in transiciones:
            print(f"  → [{destino}]  ({accion})")
    else:
        print("Estado terminal — no hay más transiciones posibles.")