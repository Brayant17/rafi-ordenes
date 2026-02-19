def menu():
    total = 0
    listaPedidos = []
    while True:
        print("Bienvenido al menú principal")
        print("1. Hamburguesa ($150)")
        print("2. Pizza ($80)")
        print("3. Ensalada ($129)")
        print("4. Tacos ($135)")
        print("5. Rollo de Sushi ($99)")
        print("Seleccione su platillo (1-5): ")

        opcion = input()
        if opcion == '1':
            print("Has seleccionado Hamburguesa. Precio: $150")
            nombrePlato = "Hamburguesa"
            precio = 150
            
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
            
        else:
            print("Opción no válida, por favor intente de nuevo.")
        
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