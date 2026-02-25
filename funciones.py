# funciones.py

# importaciones
from utils import separador

# Variables globales
ordenes = [] #Variable que es una lista que tomamos como global para listar las ordenes o diccionarios de ordenes

def menuOperaciones():
    while True:
        # menu principal
        # Este menu nos permitira hacer demas funciones (Proximamente): tenemos que hacer las funciones que faltan
        print("Bienvenido al menú principal")
        print("1-Tomar Orden")
        print("2-Ver Ordenes")
        print("3-Ganancias del dia")
        print("4-Cerrar")
        try:
            opcion = int(input())
        except ValueError:
            print("Debes de ingresar un numero")
            continue
        if opcion == 1:
            print (separador("Tomar Orden"))
            print("Listo para tomar las ordenes, se desplegara el menu a continuacion")
            menu()
        elif opcion == 2:
            print (separador("Ordenes del dia"))
            mostrarOrdenes(ordenes)
            print (separador())
        elif opcion == 3:
            print (separador("Ganancias del dia"))
            print("Ganancias del dia")
        elif opcion == 4:
            break
        else:
            print("Opcion no valida intente de nuevo")

def menu():
    # Función para mostrar el menú y procesar los pedidos
    total = 0
    listaPedidos = []
    while True:
        print("Bienvenido al menú principal")
        print("1. Hamburguesa ($150)")
        print("2. Pizza ($80)")
        print("3. Ensalada ($129)")
        print("4. Tacos ($135)")
        print("5. Rollo de Sushi ($99)")
        print("6. Enchiladas Suizas ($119)")
        print("Seleccione su platillo (1-5): ")
        print("Mi primera vez usando pyhithon :)")
        opcion = input()
        if opcion == '1':
            print("Has seleccionado Hamburguesa. Precio: $150")
            nombrePlato = "Hamburguesa"
            precio = 150
            ordenes.append(agregarOrden("Hamburguesa", precio)) #agrega una orden a la lita de ordenes
        elif opcion == '2':
            print("Has seleccionado Pizza. Precio: $80")
            nombrePlato = "Pizza"
            precio = 80
            
        elif opcion == '3':
            print("Has seleccionado Ensalada. Precio: $129")
            nombrePlato = "Ensalada"
            precio = 129
            
        elif opcion == '4':
            print("Has seleccionado Tacos. Precio: $135")
            nombrePlato = "Tacos"
            precio = 135
            
        elif opcion == '5':
            print("Has seleccionado Rollo de Sushi. Precio: $99")
            nombrePlato = "Rollo de Sushi"
            precio = 99
            
        elif opcion== '6':
            print("Has seleccionado Enchiladas Suizas. Precio: $119")
            nombrePlato = "Enchiladas Suizas"
            precio = 119
            
        else:
            print("Opción no válida, por favor intente de nuevo.")
        
        print("Seleccione su bebeida")
        print("7. Agua 600ml ($25)")
        print("8. Agua de sabor 600ml ($35)")
        print("9. Agua de sabor 1L ($45)")
        print("10. Refresco ($30)")
        opcion = input()
        if opcion == "7":
            print("Has seleccionado Agua 600ml. Precio: $25")
            nombreBebida = "Agua 600ml"
            precio = 25

        total += precio
        listaPedidos.append(nombrePlato)
        print(f"Total actual: ${total}")
        print("¿Desea agregar otro platillo? (s/n): ")
        respuesta = input().lower()
        if respuesta != 's':
            break
    
    print("--- Resumen del Pedido ---")
    print("Resumen de tu pedido:")
    for pedido in listaPedidos:
        print(f"- {pedido}")
    print(f"Total a pagar: ${total}")
    print("Gracias por su pedido.")
    print(" QUE ALEGRIA ")


# Agrega nueva orden en formato de diccionario con nombre de producto y precio
def agregarOrden(producto, precio):
    nuevaOrden = {
        "producto": producto,
        "precio": precio
    }
    return nuevaOrden

# lista las ordenes de la lista de ordenes y las separa por producto y precio en una sola linea
def mostrarOrdenes(ordenes):
    for orden in ordenes :
        print(f"{orden['producto']} ----- ${orden['precio']}")     