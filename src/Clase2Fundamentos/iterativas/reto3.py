texto = input("Escribe una frase o parrafo largo: ")

# pasar todo a minusculas para que no haya problemas de mayusculas
texto = texto.lower()

# quitar las comas, puntos y eso reemplazandolos por nada
texto = texto.replace(",", "")
texto = texto.replace(".", "")
texto = texto.replace(";", "")
texto = texto.replace("!", "")

# separar el texto por espacios para tener las palabras en una lista
palabras = texto.split()

# crear un diccionario vacio
frecuencias = {}

# contar cuantas veces aparece cada palabra
for palabra in palabras:
    if palabra in frecuencias:
        # si ya esta en el diccionario le sumo 1
        frecuencias[palabra] = frecuencias[palabra] + 1
    else:
        # si no esta la agrego con el valor 1
        frecuencias[palabra] = 1

print("\nDiccionario de palabras contadas:")
for palabra in frecuencias:
    print(f"{palabra}: {frecuencias[palabra]}")

# buscar la palabra que mas se repite
palabra_mas_repetida = ""
mayor_cantidad = 0

for palabra in frecuencias:
    if frecuencias[palabra] > mayor_cantidad:
        mayor_cantidad = frecuencias[palabra]
        palabra_mas_repetida = palabra

if mayor_cantidad > 0:
    print(f"\nLa palabra que mas aparece es '{palabra_mas_repetida}' y salio {mayor_cantidad} veces.")
else:
    print("\nNo escribiste nada.")
