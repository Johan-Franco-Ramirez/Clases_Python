#reto 3
print("Motor de Análisis de Frecuencia de Texto")

texto = input("Ingrese una frase o un párrafo: ")

texto = texto.lower()

texto = texto.replace(",", "")
texto = texto.replace(".", "")
texto = texto.replace(";", "")
texto = texto.replace("!", "")

palabras = texto.split()

frecuencias = {}

for palabra in palabras:

    if palabra in frecuencias:
        frecuencias[palabra] += 1

    else:
        frecuencias[palabra] = 1

mayor_palabra = ""
mayor_frecuencia = 0

for palabra, cantidad in frecuencias.items():

    if cantidad > mayor_frecuencia:

        mayor_frecuencia = cantidad
        mayor_palabra = palabra

print(" FRECUENCIA DE PALABRAS")

for palabra, cantidad in frecuencias.items():

    print(f"{palabra}: {cantidad}")

print(" PALABRA MAS FRECUENTE")
print(f"Palabra: {mayor_palabra}")
print(f"Cantidad: {mayor_frecuencia}")