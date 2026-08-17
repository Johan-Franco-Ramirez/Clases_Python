inventario = [
    ["Manzana", 50, 0.75],
    ["Pan", 30, 1.20],
    ["Leche", 20, 0.95],
]


def mostrar_inventario():
    print("Producto     Cantidad   Precio")
    print("-" * 30)
    for nombre, cantidad, precio in inventario:
        print(f"{nombre:12} {cantidad:8} {precio:8.2f}")


def actualizar_precio(nombre, nuevo_precio):
    for producto in inventario:
        if producto[0] == nombre:
            producto[2] = nuevo_precio
            print(f"Precio de {nombre} actualizado a {nuevo_precio:.2f}")
            return
    print(f"Producto {nombre} no encontrado")


def añadir_producto(nombre, cantidad, precio):
    for producto in inventario:
        if producto[0] == nombre:
            producto[1] += cantidad
            print(f"Stock de {nombre} actualizado a {producto[1]}")
            return
    inventario.append([nombre, cantidad, precio])
    print(f"Producto {nombre} añadido con {cantidad} unidades")


def registrar_venta(nombre, cantidad):
    for producto in inventario:
        if producto[0] == nombre:
            if producto[1] >= cantidad:
                producto[1] -= cantidad
                print(f"Venta registrada: {cantidad} x {nombre}")
            else:
                print(f"No hay stock suficiente de {nombre}")
            return
    print(f"Producto {nombre} no encontrado")


print("=== INVENTARIO INICIAL ===")
mostrar_inventario()

print("\n=== OPERACIONES ===")
actualizar_precio("Manzana", 0.90)
añadir_producto("Pan", 10, 1.20)
añadir_producto("Huevos", 12, 2.50)
registrar_venta("Leche", 5)
registrar_venta("Leche", 100)

print("\n=== INVENTARIO FINAL ===")
mostrar_inventario()
