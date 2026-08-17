kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

# 2. Convertidores

# Convertidor de tiempo a segundos
horas = int(input("Horas jugadas: "))
minutos = int(input("Minutos jugados: "))
segundos = int(input("Segundos jugados: "))

total_segundos = horas * 3600 + minutos * 60 + segundos

print("Tiempo total en segundos:", total_segundos)
print("Por qué: las horas se pasan a segundos, los minutos también y luego se suma todo.\n")


# Convertidor de moneda
dolares = float(input("Cantidad en dólares: "))
tasa = float(input("Tasa de cambio: "))

pesos = dolares * tasa

print("Valor en pesos:", round(pesos, 2))
print("Por qué: los dólares se multiplican por la tasa de cambio.\n")


# Convertidor de temperatura
celsius = float(input("Temperatura en Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperatura en Fahrenheit:", round(fahrenheit, 2))
print("Por qué: se aplica la fórmula de Celsius a Fahrenheit.\n")