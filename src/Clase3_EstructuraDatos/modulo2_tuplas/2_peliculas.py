catalogo = (
    ("El Padrino", "Francis Ford Coppola", 1972, 9.2),
    ("El Caballero Oscuro", "Christopher Nolan", 2008, 9.0),
    ("Pulp Fiction", "Quentin Tarantino", 1994, 8.9),
    ("Titanic", "James Cameron", 1997, 7.9),
    ("Inception", "Christopher Nolan", 2010, 8.8),
)


def buscar_por_director(catalogo, director):
    return tuple(p for p in catalogo if p[1].lower() == director.lower())


def obtener_estadisticas(catalogo):
    puntuaciones = [p[3] for p in catalogo]
    return (min(puntuaciones), max(puntuaciones), sum(puntuaciones) / len(puntuaciones))


print("=== CATÁLOGO DE PELÍCULAS ===")
for titulo, director, año, puntuacion in catalogo:
    print(f"{titulo} ({año}) dirigida por {director} - Puntuación: {puntuacion}")

print("\n=== OPERADOR * ===")
primera, *resto = catalogo
print("Primera película:", primera)
print("Resto:", resto)

print("\n=== BÚSQUEDA POR DIRECTOR ===")
print("Películas de Christopher Nolan:", buscar_por_director(catalogo, "Christopher Nolan"))

print("\n=== ESTADÍSTICAS ===")
minima, maxima, promedio = obtener_estadisticas(catalogo)
print(f"Puntuación mínima: {minima}")
print(f"Puntuación máxima: {maxima}")
print(f"Promedio: {promedio:.2f}")
