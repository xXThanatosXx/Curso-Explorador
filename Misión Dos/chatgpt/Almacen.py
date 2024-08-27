def mostrar_menu():
    print("Menú de la Aplicación")
    print("1. Agregar Producto")
    print("2. Editar Producto")
    print("3. Mostrar Productos")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion

def agregar_producto(productos):
    if len(productos) >= 5:
        print("Ya se han agregado 5 productos. No se pueden agregar más.")
        return
    marca = input("Ingresa la marca de la cerveza: ")
    precio = float(input("Ingresa el precio de la cerveza: "))
    iva = precio * 0.21
    precio_con_iva = precio + iva
    producto = {
        "marca": marca,
        "precio": precio,
        "iva": iva,
        "precio_con_iva": precio_con_iva
    }
    productos.append(producto)
    print("Producto agregado correctamente.")

def editar_producto(productos):
    if not productos:
        print("No hay productos para editar.")
        return
    mostrar_productos(productos)
    indice = int(input("Selecciona el número del producto que deseas editar: ")) - 1
    if indice < 0 or indice >= len(productos):
        print("Índice inválido.")
        return
    marca = input("Ingresa la nueva marca de la cerveza: ")
    precio = float(input("Ingresa el nuevo precio de la cerveza: "))
    iva = precio * 0.21
    precio_con_iva = precio + iva
    productos[indice] = {
        "marca": marca,
        "precio": precio,
        "iva": iva,
        "precio_con_iva": precio_con_iva
    }
    print("Producto editado correctamente.")

def mostrar_productos(productos):
    if not productos:
        print("No hay productos para mostrar.")
        return
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. Marca: {producto['marca']}, Precio: {producto['precio']:.2f}, IVA: {producto['iva']:.2f}, Precio con IVA: {producto['precio_con_iva']:.2f}")
