def mostrar_menu():
    print("\nBienvenido al sistema de inventario de la tienda.")
    print("1. Agregar un producto al inventario")
    print("2. Vender un producto")
    print("3. Mostrar inventario")
    print("4. Salir")
    opcion = input("\nElige una opción: ")
    return opcion

def agregar_producto(inventario):
    nombre_producto = input("Ingresa el nombre del producto: ")
    cantidad = int(input(f"Ingresa la cantidad de {nombre_producto}: "))
    if nombre_producto in inventario:
        inventario[nombre_producto] += cantidad
    else:
        inventario[nombre_producto] = cantidad
    print("\nProducto agregado al inventario.")

def vender_producto(inventario):
    nombre_producto = input("Ingresa el nombre del producto a vender: ")
    if nombre_producto in inventario:
        cantidad = int(input(f"Ingresa la cantidad a vender de {nombre_producto}: "))
        if cantidad <= inventario[nombre_producto]:
            inventario[nombre_producto] -= cantidad
            print("\nVenta realizada.")
        else:
            print("\nNo hay suficiente stock.")
    else:
        print("\nEl producto no existe en el inventario.")

def mostrar_inventario(inventario):
    print("\nInventario:")
    for producto, cantidad in inventario.items():
        print(f"- {producto}: {cantidad}")

def main():
    inventario = {}
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            vender_producto(inventario)
        elif opcion == "3":
            mostrar_inventario(inventario)
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, elige una opción del 1 al 4.")

if __name__ == "__main__":
    main()
