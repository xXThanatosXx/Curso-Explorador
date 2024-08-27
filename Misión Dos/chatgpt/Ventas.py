import Almacen as vent

def main():
    productos = []
    while True:
        opcion = vent.mostrar_menu()
        if opcion == "1":
            vent.agregar_producto(productos)
        elif opcion == "2":
            vent.editar_producto(productos)
        elif opcion == "3":
            vent.mostrar_productos(productos)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
