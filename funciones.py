def menu():
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
            break
        elif opcion == '2':
            print("Has seleccionado Pizza. Precio: $80")
            break
        elif opcion == '3':
            print("Has seleccionado Ensalada. Precio: $129")
            break
        elif opcion == '4':
            print("Has seleccionado Tacos. Precio: $135")
            break
        elif opcion == '5':
            print("Has seleccionado Rollo de Sushi. Precio: $99")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
        