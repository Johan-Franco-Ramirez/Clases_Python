# esto es para pedir los datos del programador
nombre = input("Ingresa tu nombre: ")
proyectos = int(input("Cuantos proyectos tienes asignados?: "))

# listas y variables para guardar cosas
horas_por_proyecto = []
total_horas = 0
contador = 1

# ciclo para pedir las horas de cada proyecto
while contador <= proyectos:
    horas = float(input(f"Horas que le dedicaste al proyecto {contador}: "))
    horas_por_proyecto.append(horas)
    total_horas = total_horas + horas
    contador = contador + 1

# calculo del promedio
if proyectos > 0:
    promedio = total_horas / proyectos
else:
    promedio = 0

print("")
print(f" Reporte de {nombre} ")
print(f"Total de horas trabajadas: {total_horas}")
print(f"Promedio de horas por proyecto: {promedio}")
print("")
print("Proyecto   | Horas   | Porcentaje")

# otro ciclo para mostrar los porcentajes
posicion = 0
while posicion < proyectos:
    if total_horas > 0:
        porcentaje = (horas_por_proyecto[posicion] / total_horas) * 100
    else:
        porcentaje = 0
        
    numero_proyecto = posicion + 1
    # imprimiendo cada fila con f-strings normales sin formatos complicados
    print(f"Proyecto {numero_proyecto} | {horas_por_proyecto[posicion]} hrs | {porcentaje}%")
    posicion = posicion + 1
