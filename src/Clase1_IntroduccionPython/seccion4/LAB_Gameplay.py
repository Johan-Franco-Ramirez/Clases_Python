# LAB - Ejercicios de Algoritmos
# Mecánicas de Gameplay

# 1. Puntaje total
nivel1 = float(input("Puntos del nivel 1: "))
nivel2 = float(input("Puntos del nivel 2: "))
nivel3 = float(input("Puntos del nivel 3: "))

total_puntos = nivel1 + nivel2 + nivel3
print("Puntaje total:", total_puntos)
print("Por qué: se suman los puntos obtenidos en los tres niveles.\n")


# 2. Tiempo total de juego en segundos
horas = int(input("Horas jugadas: "))
minutos = int(input("Minutos jugados: "))
segundos = int(input("Segundos jugados: "))

total_segundos = horas * 3600 + minutos * 60 + segundos
print("Tiempo total en segundos:", total_segundos)
print("Por qué: las horas y minutos se convierten a segundos y luego se suman.\n")


# 3. Daño total
ataque1 = float(input("Daño del ataque 1: "))
ataque2 = float(input("Daño del ataque 2: "))
ataque3 = float(input("Daño del ataque 3: "))

daño_total = ataque1 + ataque2 + ataque3
print("Daño total:", daño_total)
print("Por qué: se suma el daño de los tres ataques.\n")


# 4. Experiencia total
xp1 = float(input("Experiencia de la misión 1: "))
xp2 = float(input("Experiencia de la misión 2: "))
xp3 = float(input("Experiencia de la misión 3: "))

xp_total = xp1 + xp2 + xp3
print("Experiencia total:", xp_total)
print("Por qué: la experiencia de las tres misiones se acumula.\n")


# 5. Porcentaje de vida restante
vida_maxima = float(input("Vida máxima: "))
vida_actual = float(input("Vida actual: "))

porcentaje_vida = (vida_actual / vida_maxima) * 100
print("Vida restante:", round(porcentaje_vida, 2), "%")
print("Por qué: la vida actual se divide entre la máxima y se multiplica por 100.\n")


# 6. Oro total
oro1 = float(input("Oro de la misión 1: "))
oro2 = float(input("Oro de la misión 2: "))
oro3 = float(input("Oro de la misión 3: "))

oro_total = oro1 + oro2 + oro3
print("Oro total:", oro_total)
print("Por qué: se suma todo el oro recolectado.\n")


# 7. Velocidad promedio
distancia = float(input("Distancia recorrida: "))
tiempo = float(input("Tiempo utilizado: "))

velocidad = distancia / tiempo
print("Velocidad promedio:", velocidad)
print("Por qué: la velocidad se calcula dividiendo distancia entre tiempo.\n")


# 8. Costo total de mejoras
mejora1 = float(input("Costo de la mejora 1: "))
mejora2 = float(input("Costo de la mejora 2: "))
mejora3 = float(input("Costo de la mejora 3: "))

costo_mejoras = mejora1 + mejora2 + mejora3
print("Costo total de mejoras:", costo_mejoras)
print("Por qué: se suman los precios de las tres mejoras.\n")


# 9. Tiempo restante de una misión
tiempo_total = float(input("Tiempo total de la misión: "))
tiempo_transcurrido = float(input("Tiempo transcurrido: "))

tiempo_restante = tiempo_total - tiempo_transcurrido
print("Tiempo restante:", tiempo_restante)
print("Por qué: al tiempo total se le resta el tiempo que ya pasó.\n")


# 10. Nivel promedio del equipo
jugador1 = float(input("Nivel del jugador 1: "))
jugador2 = float(input("Nivel del jugador 2: "))
jugador3 = float(input("Nivel del jugador 3: "))

nivel_promedio = (jugador1 + jugador2 + jugador3) / 3
print("Nivel promedio:", nivel_promedio)
print("Por qué: se suman los niveles y se dividen entre tres jugadores.\n")


# 11. Daño crítico
daño_base = float(input("Daño base: "))
multiplicador = float(input("Multiplicador crítico: "))

daño_critico = daño_base * multiplicador
print("Daño crítico:", daño_critico)
print("Por qué: el daño base se multiplica por el multiplicador crítico.\n")


# 12. Tiempo en horas y minutos
minutos_totales = int(input("Minutos totales jugados: "))

horas_juego = minutos_totales // 60
minutos_juego = minutos_totales % 60

print("Tiempo de juego:", horas_juego, "horas y", minutos_juego, "minutos")
print("Por qué: // obtiene las horas completas y % los minutos que sobran.\n")


# 13. Porcentaje de misiones completadas
misiones_totales = float(input("Misiones totales: "))
misiones_completadas = float(input("Misiones completadas: "))

porcentaje_misiones = (misiones_completadas / misiones_totales) * 100
print("Misiones completadas:", round(porcentaje_misiones, 2), "%")
print("Por qué: se divide las misiones completadas entre el total y se multiplica por 100.\n")


# 14. Costo de objetos
objeto1 = float(input("Costo del objeto 1: "))
objeto2 = float(input("Costo del objeto 2: "))
objeto3 = float(input("Costo del objeto 3: "))

costo_total = objeto1 + objeto2 + objeto3
print("Costo total de objetos:", costo_total)
print("Por qué: se suman los tres precios de la tienda.\n")


# 15. Tiempo promedio de partidas
partida1 = float(input("Tiempo de la partida 1: "))
partida2 = float(input("Tiempo de la partida 2: "))
partida3 = float(input("Tiempo de la partida 3: "))

tiempo_promedio = (partida1 + partida2 + partida3) / 3
print("Tiempo promedio:", tiempo_promedio)
print("Por qué: se suman los tiempos y se dividen entre tres partidas.\n")


# 16. Porcentaje de enemigos derrotados
enemigos_totales = float(input("Enemigos totales: "))
enemigos_derrotados = float(input("Enemigos derrotados: "))

porcentaje_enemigos = (enemigos_derrotados / enemigos_totales) * 100
print("Enemigos derrotados:", round(porcentaje_enemigos, 2), "%")
print("Por qué: se compara la cantidad derrotada con el total de enemigos.\n")