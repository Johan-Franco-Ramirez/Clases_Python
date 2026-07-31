# ejemplo de conjuntos en tiendas
tienda_centro = {
    "Laptop",
    "Mouse",
    "Teclado"
}

tienda_norte = {
    "Mouse",
    "Monitor"
}

tienda_sur = {
    "Tablet",
    "Camara",
}

#ejemplo del uso addecuado
print("\nAgregar un producto")

tienda_centro.add("Impresora")

print(tienda_centro)


print("\nAgregar varios productos")

tienda_norte.update(["Audifonos", "Parlantes"]) #uso de .update

print(tienda_norte)

tienda_sur.update(["tripode","gabinete pc"])

print(tienda_sur)
#el uso de eliminar (remove)

print("\nEliminar un producto existente")

tienda_norte.remove("Mouse")

print(tienda_norte)

#el uso discreto del discard sin la aparicion de error

print("\nEliminar un producto que puede no existir")

tienda_sur.discard("Consola")

print(tienda_sur)

# uso de pop() aleatorio para eliminar

print("\nEliminar un elemento cualquiera")

eliminado = tienda_sur.pop()

print("Elemento eliminado: ", eliminado)
print(tienda_sur)

#se vacia una copia del conjunto tienda

print("\nVaciar una copia del conjunto")

copia = tienda_norte.copy()

copia.clear()

print("Original: ", tienda_norte)
print("Copia: ", copia)

# union basica 

catalogo = tienda_centro.union(tienda_norte)

print("\nUnion")
print(catalogo)

#interseccion basica

print("\nInterseccion")

print(tienda_centro.intersection(tienda_norte))

#diferencias usando el metodo normal
print("\nDiferencia")

print(tienda_centro.difference(tienda_norte))

#usando un symmetric para diferencias 

print("\nDiferencia simétrica")

print(tienda_centro.symmetric_difference(tienda_norte))

#uso del .isdisjoint

print("\n¿No tienen elementos en común?")

print(tienda_centro.isdisjoint(tienda_sur))

# uso del issubset

print("\n¿Es subconjunto?")

print({"Laptop"} <= tienda_centro)

# También con el método

print({"Laptop"}.issubset(tienda_centro))

# otro ejemplo de uso issuperset()

print("\n¿Es superconjunto?")

print(tienda_centro.issuperset({"Laptop"}))

# usuarios y generos

usuario1 = {
    "Acción",
    "Comedia",
    "Ciencia ficción",
    "Aventura",
    "Animación"
}

usuario2 = {
    "Drama",
    "Comedia",
    "Romance",
    "Acción",
    "Terror"
}

usuario3 = {
    "Acción",
    "Aventura",
    "Fantasía",
    "Ciencia ficción"
}

# operadores entre conjuntos

comunes = usuario1 & usuario2

universo = usuario1 | usuario2 | usuario3

solo_usuario1 = usuario1 - usuario2

diferencias = usuario2 ^ usuario3

# Diferencia simétrica
diferencias2 = usuario2.symmetric_difference(usuario3)

#subconjuntos y superconjuntos

print("\n¿Usuario3 es subconjunto de Usuario1?")
print(usuario3 <= usuario1)

print("\n¿{'Acción', 'Aventura'} es subconjunto de Usuario1?")
print({"Acción", "Aventura"} <= usuario1)

print("\nUsando issubset()")
print({"Acción", "Aventura"}.issubset(usuario1))

print("\n¿Usuario1 es superconjunto de {'Acción', 'Aventura'}?")
print(usuario1.issuperset({"Acción", "Aventura"}))

# resultados 

print("\n---Recomendaciones---")

print("\nGéneros comunes: ")
print(comunes)

print("\nTodos los géneros: ")
print(universo)

print("\nExclusivos Usuario1: ")
print(solo_usuario1)

print("\nDiferencia simétrica (^): ")
print(diferencias)

print("\nDiferencia simétrica (symmetric_difference): ")
print(diferencias2)