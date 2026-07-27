# con libreria

print(" Calculadora de Métricas del Desarrollador ")

nom_des = input("Ingrese el nombre del desarrollador: ")

cant_proy = int(input("¿Cuántos proyectos tiene asignados?: "))

horas_proy = []

for i in range(cant_proy):
    horas = float(input(f"Ingrese las horas del proyecto {i+1}: "))
    horas_proy.append(horas)

total_horas = sum(horas_proy)

prom_h = total_horas / cant_proy

print("REPORTE")
print(f"Desarrollador: {nom_des}")
print(f"Total de horas: {total_horas}")
print(f"Promedio por proyecto: {prom_h:.2f}\n")

print("Proyecto\tHoras\tPorcentaje")

for i, horas in enumerate(horas_proy):
    porcentaje = (horas / total_horas) * 100
    print(f"{i+1}\t\t{horas}\t{porcentaje:.2f}%")


# con diccionario

print("Calculadora de Métricas del Desarrollador v.2")

nom_dev = input("Ingrese el nombre del desarrollador: ")

num_proy = int(input("¿Cuántos proyectos tiene asignados?: "))

proyectos_dev = {}

for i in range(num_proy):

    nom_proy = input(f"Nombre del proyecto {i+1}: ")

    horas_trabajadas = float(
        input(f"Horas dedicadas al proyecto '{nom_proy}': ")
    )

    proyectos_dev[nom_proy] = horas_trabajadas

total_general = sum(proyectos_dev.values())

promedio_general = total_general / num_proy

print("REPORTE")
print(f"Desarrollador: {nom_dev}")
print(f"Total de horas: {total_general}")
print(f"Promedio por proyecto: {promedio_general:.2f}\n")

print("Proyecto\tHoras\tPorcentaje")

for proyecto, hora in proyectos_dev.items():

    porcentaje = (hora / total_general) * 100

    print(f"{proyecto}\t{hora}\t{porcentaje:.2f}%")