tienda_centro = {"pan", "leche", "huevos", "arroz", "cafe"}
tienda_norte = {"arroz", "cafe", "azucar", "fideos", "queso"}
tienda_sur = {"pan", "queso", "vino", "mantequilla", "cafe"}

print("=== CATÁLOGOS DE TIENDAS ===")
catalogo_completo = tienda_centro.union(tienda_norte, tienda_sur)
productos_comunes = tienda_centro.intersection(tienda_norte, tienda_sur)
print("Catálogo completo:", catalogo_completo)
print("Productos en las tres tiendas:", productos_comunes)

print("\n=== PRODUCTOS EXCLUSIVOS ===")
solo_centro = tienda_centro.difference(tienda_norte, tienda_sur)
solo_norte = tienda_norte.difference(tienda_centro, tienda_sur)
solo_sur = tienda_sur.difference(tienda_centro, tienda_norte)
print("Exclusivos de centro:", solo_centro)
print("Exclusivos de norte:", solo_norte)
print("Exclusivos de sur:", solo_sur)

print("\n=== SOLAPAMIENTOS ===")
print("¿Centro y Norte no comparten nada?", tienda_centro.isdisjoint(tienda_norte))
print("¿Norte y Sur no comparten nada?", tienda_norte.isdisjoint(tienda_sur))

usuario1 = {"accion", "ciencia ficcion", "drama", "thriller"}
usuario2 = {"comedia", "drama", "animacion", "romance"}
usuario3 = {"accion", "drama", "terror", "documental"}

print("\n=== GÉNEROS DE USUARIOS ===")
comunes = usuario1 & usuario2 & usuario3
universo = usuario1 | usuario2 | usuario3
exclusivos1 = usuario1 - (usuario2 | usuario3)
exclusivos2 = usuario2 - (usuario1 | usuario3)
exclusivos3 = usuario3 - (usuario1 | usuario2)
solo_1_2 = usuario1 ^ usuario2
print("Géneros comunes a los tres:", comunes)
print("Universo de géneros:", universo)
print("Exclusivos de usuario1:", exclusivos1)
print("Exclusivos de usuario2:", exclusivos2)
print("Exclusivos de usuario3:", exclusivos3)
print("Diferencias usuario1 vs usuario2:", solo_1_2)

favoritos_usuario1 = {"accion", "ciencia ficcion", "drama"}
print("¿favoritos_usuario1 es subconjunto de usuario1?", favoritos_usuario1 <= usuario1)

print("\n=== RESUMEN FINAL INTEGRADO ===")
print(f"{len(catalogo_completo)} productos únicos en total entre las tiendas")
print(f"Géneros recomendados al usuario1: {universo - usuario1}")
