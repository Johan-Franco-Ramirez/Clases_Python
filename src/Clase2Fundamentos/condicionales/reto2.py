# lista del stock
stock = [12, 0, 5, 23, 2, 0, 8]

# listas vacias para guardar los que estan agotados y criticos
productos_agotados = []
total_criticos = []

total_productos = len(stock)
disponibles = 0
posicion = 0 # para saber en que indice de la lista vamos

print("Clasificacion de los productos:")

for cantidad in stock:
    if cantidad == 0:
        print(f"Producto {posicion}: Agotado - Reorden Inmediata")
        productos_agotados.append(posicion)
    elif cantidad >= 1 and cantidad <= 5:
        print(f"Producto {posicion}: Crítico - Reposición Sugerida")
        total_criticos.append(cantidad)
        disponibles = disponibles + 1
    elif cantidad > 5:
        print(f"Producto {posicion}: Adecuado")
        disponibles = disponibles + 1
        
    posicion = posicion + 1 # sumamos 1 a la posicion para el siguiente ciclo

# calcular porcentaje de los que si hay
porcentaje = (disponibles / total_productos) * 100

print("")
print("Resumen:")
print(f"Indices de productos agotados: {productos_agotados}")
print(f"Valores de stock criticos: {total_criticos}")
print(f"Porcentaje de disponibilidad: {porcentaje}%")
