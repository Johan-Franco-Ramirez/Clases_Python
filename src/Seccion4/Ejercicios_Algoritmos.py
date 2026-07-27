#Ejercicios 1-16 :,) 

#1
print(" 'Ejercicio 1'")

nivel1= int(input("Ingrese puntaje del primer nivel: "))
nivel2= int(input("Ingrese puntaje del segundo nivel: "))
nivel3= int(input("Ingrese puntaje del tercer nivel: "))

puntaje_total= nivel1+nivel2+nivel3

print("Su puntaje total es de: ", puntaje_total)

#2
print(" 'Ejercicio 2'")

h = int(input("Ingrese las horas jugadas: "))
min = int(input("Ingrese los minutos jugados: "))
seg = int(input("Ingrese los segundos jugados: "))

tiempo_total = (h * 3600) + (min * 60) + seg

print("El tiempo total jugado es:", tiempo_total, "seg")

#3
print(" 'Ejercicio 3'")

ataq1 = int(input("Ingrese el daño del primer ataque: "))
ataq2 = int(input("Ingrese el daño del segundo ataque: "))
ataq3 = int(input("Ingrese el daño del tercer ataque: "))

dano_total = ataq1 + ataq2 + ataq3

print("El daño total causado es: ", dano_total)

#4
print(" 'Ejercicio 4'")

mis1 = int(input("Ingrese la experiencia obtenida en la misión 1: "))
mis2 = int(input("Ingrese la experiencia obtenida en la misión 2: "))
mis3 = int(input("Ingrese la experiencia obtenida en la misión 3: "))

experiencia_total = mis1 + mis2 + mis3

print("La experiencia total ganada es: ", experiencia_total, "XP")

#5
print(" 'Ejercicio 5'")

vida_max = float(input("Ingrese la vida máxima del personaje: "))
vida_act = float(input("Ingrese la vida actual del personaje: "))

porcentaje_vida = (vida_act / vida_max) * 100

print("El porcentaje de vida restante es: ", porcentaje_vida, "%")

#6
print(" 'Ejercicio 6'")

oro1 = int(input("Ingrese el oro recolectado en la misión 1: "))
oro2 = int(input("Ingrese el oro recolectado en la misión 2: "))
oro3 = int(input("Ingrese el oro recolectado en la misión 3: "))

oro_total = oro1 + oro2 + oro3

print("El oro total recolectado es: ", oro_total)

#7
print(" 'Ejercicio 7'")

dis = float(input("Ingrese la distancia recorrida (km): "))
tiem = float(input("Ingrese el tiempo empleado (horas): "))

velocidad_promedio = dis / tiem

print("La velocidad promedio del vehículo es: ", velocidad_promedio, "km/h")

#8
print(" 'Ejercicio 8'")

mejora1 = float(input("Ingrese el costo de la primera mejora: "))
mejora2 = float(input("Ingrese el costo de la segunda mejora: "))
mejora3 = float(input("Ingrese el costo de la tercera mejora: "))

costo_total = mejora1 + mejora2 + mejora3

print("El costo total de las mejoras es: ", costo_total)

#9
print(" 'Ejercicio 9'")

tiempo_total = float(input("Ingrese el tiempo total de la misión (min): "))
tiempo_transcurrido = float(input("Ingrese el tiempo transcurrido (min): "))

tiempo_restante = tiempo_total - tiempo_transcurrido

print("El tiempo restante para completar la misión es: ", tiempo_restante, "min")

#10
print(" 'Ejercicio 10'")

jugador1 = int(input("Ingrese el nivel del jugador 1: "))
jugador2 = int(input("Ingrese el nivel del jugador 2: "))
jugador3 = int(input("Ingrese el nivel del jugador 3: "))

nivel_promedio = (jugador1 + jugador2 + jugador3) / 3

print("El nivel promedio del equipo es: ", nivel_promedio)

#11
print(" 'Ejercicio 11'")

dano_base = float(input("Ingrese el daño base del ataque: "))
multiplicador_critico = float(input("Ingrese el multiplicador crítico: "))

dano_critico = dano_base * multiplicador_critico

print("El daño crítico causado es: ", dano_critico)

#12
print(" 'Ejercicio 12'")

min_totales = int(input("Ingrese el tiempo total jugado en minutos: "))

h1 = min_totales // 60
minutos = min_totales % 60

print("El tiempo total de juego es: ", h1, "horas y", minutos, "minutos")

#13
print(" 'Ejercicio 13'")

total_misiones = int(input("Ingrese el número total de misiones: "))
misiones_completadas = int(input("Ingrese el número de misiones completadas: "))

porcentaje_completado = (misiones_completadas / total_misiones) * 100

print("El porcentaje de misiones completadas es: ", porcentaje_completado, "%")

# 14
print(" 'Ejercicio 14'")

obj1 = float(input("Ingrese el costo del primer objeto: "))
obj2 = float(input("Ingrese el costo del segundo objeto: "))
obj3 = float(input("Ingrese el costo del tercer objeto: "))

costo_total = obj1 + obj2 + obj3

print("El costo total de los objetos comprados es: ", costo_total)

# 15
print(" 'Ejercicio 15'")

partida1 = float(input("Ingrese el tiempo de la primera partida (minutos): "))
partida2 = float(input("Ingrese el tiempo de la segunda partida (minutos): "))
partida3 = float(input("Ingrese el tiempo de la tercera partida (minutos): "))

tiem_promedio = (partida1 + partida2 + partida3) / 3

print("El tiempo promedio de las partidas es: ", tiem_promedio, "minutos")

#16
print(" 'Ejercicio 16")

total_enemigos = int(input("Ingrese el número total de enemigos: "))
enemigos_derrotados = int(input("Ingrese el número de enemigos derrotados: "))

porcentaje_derrotados = (enemigos_derrotados / total_enemigos) * 100

print("El porcentaje de enemigos derrotados es: ", porcentaje_derrotados, "%")

