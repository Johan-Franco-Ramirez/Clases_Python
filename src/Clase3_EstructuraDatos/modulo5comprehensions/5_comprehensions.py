ventas = [
    {"nombre": "Café", "precio": 5.50, "unidades": 120, "categoria": "Bebidas"},
    {"nombre": "Televisor", "precio": 480.00, "unidades": 25, "categoria": "Electrónica"},
    {"nombre": "Smartphone", "precio": 650.00, "unidades": 18, "categoria": "Electrónica"},
    {"nombre": "Té", "precio": 3.00, "unidades": 80, "categoria": "Bebidas"},
    {"nombre": "Galletas", "precio": 2.50, "unidades": 200, "categoria": "Snacks"},
    {"nombre": "Auriculares", "precio": 55.00, "unidades": 40, "categoria": "Electrónica"},
    {"nombre": "Queso", "precio": 8.00, "unidades": 60, "categoria": "Lácteos"},
    {"nombre": "Chocolate", "precio": 4.00, "unidades": 150, "categoria": "Snacks"},
    {"nombre": "Pan", "precio": 1.20, "unidades": 500, "categoria": "Panadería"},
    {"nombre": "Leche", "precio": 0.90, "unidades": 300, "categoria": "Lácteos"},
]

print("=== LIST COMP: VALOR TOTAL POR PRODUCTO ===")
valor_total = [p["unidades"] * p["precio"] for p in ventas]
print(valor_total)

print("\n=== LIST COMP CON FILTRO: VALOR > 1000 ===")
productos_top = [p["nombre"] for p in ventas if p["unidades"] * p["precio"] > 1000]
print(productos_top)

print("\n=== DICT COMP: PRODUCTO_INFO ===")
producto_info = {
    p["nombre"]: {"valor": p["unidades"] * p["precio"], "unidades": p["unidades"]}
    for p in ventas
}
for nombre, info in producto_info.items():
    print(f"{nombre}: {info}")

print("\n=== DICT COMP CON FILTRO: RANKING PREMIUM (precio > 50) ===")
ranking_premium = {p["nombre"]: p["unidades"] * p["precio"] for p in ventas if p["precio"] > 50}
ranking_premium = dict(
    sorted(ranking_premium.items(), key=lambda item: item[1], reverse=True)
)
for nombre, valor in ranking_premium.items():
    print(f"{nombre}: {valor}")

print("\n=== SET COMP ===")
categorias_unicas = {p["categoria"] for p in ventas}
productos_baratos = {p["nombre"] for p in ventas if p["precio"] <= 50}
print("Categorías únicas:", categorias_unicas)
print("Productos baratos:", productos_baratos)

print("\n=== COMBINACIÓN ===")
resumen_formateado = [
    f"{nombre}: valor {info['valor']} (unidades: {info['unidades']})"
    for nombre, info in producto_info.items()
]
gran_total = sum(valor_total)
for linea in resumen_formateado:
    print(linea)
print(f"Gran total: {gran_total}")
