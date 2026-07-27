#reto 2
print("Sistema Simplificado de Calificación e Inventario")

stock = [12, 0, 5, 23, 2, 0, 8]

prod_agotados = []
prod_criticos = []

disponibles = 0

print(" REPORTE DEL INVENTARIO")

for indice, cantidad in enumerate(stock):

    if cantidad == 0:
        estado = "Agotado Reorden Inmediata"
        prod_agotados.append(indice)

    elif 1 <= cantidad <= 5 or cantidad ==5:
        estado = "Critico Reposicion Sugerida"
        prod_criticos.append(cantidad)
        disponibles += 1

    elif cantidad > 5 :
        estado = "Adecuado"
        disponibles += 1

    else:
        print ("cantidad invalida")

    print(f"Producto {indice}\tStock: {cantidad}\tEstado: {estado}")

porcentaje = (disponibles / len(stock)) * 100

print(" RESUMEN")
print(f"Productos agotados (indices): {prod_agotados}")
print(f"Stock critico: {prod_criticos}")
print(f"Disponibilidad general: {porcentaje:.2f}%")