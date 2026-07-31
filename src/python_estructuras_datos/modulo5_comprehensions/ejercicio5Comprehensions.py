# un analizador usando comprehensions

# Definir ventas
ventas = [
    {"producto": "Laptop",      "unidades": 20, "precio": 800, "categoria": "Tecnología"},
    {"producto": "Teclado",     "unidades": 50, "precio": 25,  "categoria": "Accesorios"},
    {"producto": "Mouse",       "unidades": 30, "precio": 15,  "categoria": "Accesorios"},
    {"producto": "Monitor",     "unidades": 10, "precio": 200, "categoria": "Tecnología"},
    {"producto": "Impresora",   "unidades": 8,  "precio": 150, "categoria": "Oficina"},
    {"producto": "Parlantes",   "unidades": 15, "precio": 45,  "categoria": "Audio"}
]

#tipos de lista con comprehensions

# Valor total por producto
valor_total = [
    producto["unidades"] * producto["precio"]
    for producto in ventas
]

print("---Valor total por producto---")
print(valor_total)

# Productos destacados
productos_destacados = [
    producto["producto"]
    for producto in ventas
    if producto["unidades"] * producto["precio"] > 1000
]

print("\n---Productos destacados---")
print(productos_destacados)

# dict 

# información de productos
producto_info = {
    producto["producto"]: {
        "valor": producto["unidades"] * producto["precio"],
        "unidades": producto["unidades"]
    }
    for producto in ventas
}

print("\n---Información de productos---")
print(producto_info)

# Ranking premium
ranking_premium = {
    producto["producto"]:
    producto["unidades"] * producto["precio"]

    for producto in sorted(
        ventas,
        key=lambda p: p["unidades"] * p["precio"],
        reverse=True
    )

    if producto["precio"] > 50
}

print("\n---Ranking Premium---")
print(ranking_premium)

# set

# categorías únicas
categorias_unicas = {
    producto["categoria"]
    for producto in ventas
}

print("\n---Categorías únicas---")
print(categorias_unicas)

#productos baratos
productos_baratos = {
    producto["producto"]
    for producto in ventas
    if producto["precio"] <= 50
}

print("\n---Productos baratos---")
print(productos_baratos)

# resumen

resumen_formateado = {
    producto["producto"]:
    f'{producto["unidades"]} unidades - ${producto["unidades"] * producto["precio"]}'

    for producto in ventas
}

print("\n---Resumen---")
print(resumen_formateado)

# total 

gran_total = sum(valor_total)

print("\n---Total---")
print(gran_total)