#lista de funciones con 3 productos
Inventario = [ 
["mouse bt",23,45000],
["teclado led",10,80000],
["mouse pad",18,39000]
]

#funcion para actualizar precios de productos
def actualizar_precio(producto, nuevo_precio):

    encontrado = False

    for item in Inventario:

        if item[0].lower() == producto.lower():
            item[2] = nuevo_precio
            print(f"El precio de {producto} fue actualizado a ${nuevo_precio}")
            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado.")

#funcion para registrar ventas
def registrar_ventas(producto,cantidad):
    encontrado = False

    for item in Inventario:

        if item[0].lower() == producto.lower():

            encontrado = True

            if item[1] >= cantidad:
                item[1] -= cantidad
                print(f"Venta realizada. Se vendieron {cantidad} unidades de {producto}.")
            else:
                print("No hay suficiente stock.")

            break

    if not encontrado:
        print("Producto no encontrado.")

    

#funcion que ayuda a agregar productos a la lista
def anadir_producto(producto,cantidad,precio):
    encontrado = False

    for item in Inventario:

        if item[0].lower() == producto.lower():
            item[1] += cantidad
            print(f"Se agregaron {cantidad} unidades de {producto}.")
            encontrado = True
            break

    if not encontrado:
        Inventario.append([producto, cantidad, precio])
        print(f"Producto {producto} agregado al inventario.")


#funcion para imprimir los productos
def ver_inventario():
    print("---Inventario---")

    for producto in Inventario:
        print(f"nombre: ", producto[0])
        print(f"cantidad: ", producto[1])
        print(f"precio: ", producto[2])
        print("---"*3)
    
#pruebas
actualizar_precio("teclado led",95000)

registrar_ventas("mouse pad",1 )

anadir_producto("Bafles",5,55000)

ver_inventario()