#tupla y subtuplas para el catalogo
catalogo = (
    ("Interestelar", "Christopher Nolan", 2014, 9.5),
    ("Titanic", "James Cameron", 1997, 8.8),
    ("Avatar", "James Cameron", 2009, 8.6),
    ("El Padrino", "Francis Ford Coppola", 1972, 9.8),
    ("Inception", "Christopher Nolan", 2010, 9.4)
)

#se imprimen los catalogos

print("---Catalogo---")

for titulo, director, año, puntuacion in catalogo:
    print(f"Título: {titulo}")
    print(f"Director: {director}")
    print(f"Año: {año}")
    print(f"Puntuación: {puntuacion}")
    print("---"*4)


#se imprime la primera pelicula 

primera, *resto = catalogo

print("\nPrimera pelicula: ")
print(primera)

print("\nResto del catalogo: ")
for pelicula in resto:
    print(pelicula)


#para buscar por el director de la pelicula

def buscar_director(director):

    coincidencias = ()

    for pelicula in catalogo:

        if pelicula[1].lower() == director.lower():
            coincidencias += (pelicula,)

    return coincidencias


# por estadisticas

def obtener_estadisticas(peliculas):

    puntuaciones = ()

    for pelicula in peliculas:
        puntuaciones += (pelicula[3],)

    return (
        min(puntuaciones),
        max(puntuaciones),
        sum(puntuaciones) / len(puntuaciones)
    )


#ejemplo de la busqueda de director

resultado = buscar_director("Christopher Nolan")

print("\n---Peliculas encontradas---")

for titulo, director, año, puntuacion in resultado:
    print(f"{titulo} - {director} ({año}) - {puntuacion}")


#resultado segun estadisticas

minima, maxima, promedio = obtener_estadisticas(catalogo)

print("\n---Estadísticas---")
print("Puntuación mínima: ", minima)
print("Puntuación máxima: ", maxima)
print("Promedio: ", round(promedio, 2))