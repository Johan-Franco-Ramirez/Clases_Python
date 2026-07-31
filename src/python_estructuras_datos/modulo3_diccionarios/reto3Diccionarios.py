# Diccionarios y su funcion para ventas por regiones
ventas_region = {
    "Norte": {
        "Q1": 15000,
        "Q2": 18000,
        "Q3": 17000,
        "Q4": 20000
    },

    "Sur": {
        "Q1": 12000,
        "Q2": 14000,
        "Q3": 16000,
        "Q4": 18000
    },

    "Centro": {
        "Q1": 20000,
        "Q2": 22000,
        "Q3": 21000,
        "Q4": 25000
    },

    "Occidente": {
        "Q1": 10000,
        "Q2": 11000,
        "Q3": 13000,
        "Q4": 15000
    }
}

# calcula los valores totales
totales = {}

for region, ventas in ventas_region.items():
    totales[region] = sum(ventas.values())

print("---Totales por region---")

for region, total in totales.items():
    print(region, ":", total)

#la region con mayor venta
mejor_region = max(totales, key=lambda region: totales[region])

print("\nRegion con mayores ventas:", mejor_region)
print("Total:", totales[mejor_region])

#el total cada trimestre

totales_trimestre = {
    "Q1": 0,
    "Q2": 0,
    "Q3": 0,
    "Q4": 0
}

for region, ventas in ventas_region.items():

    for trimestre, valor in ventas.items():
        totales_trimestre[trimestre] += valor

print("\n---Totales por trimestre---")

for trimestre, total in totales_trimestre.items():
    print(trimestre, ":", total)

#total de todo
gran_total = sum(totales.values())

print("\nGran total:", gran_total)

# regiones y sus porcentajes

porcentajes = {
    region: round(total / gran_total * 100, 2)
    for region, total in totales.items()
}

print("\n---Porcentajes---")

for region, porcentaje in porcentajes.items():
    print(region, ":", porcentaje, "%")

#reporte ordenado

print("\n---Reporte Final---")

for region, total in sorted(
    totales.items(),
    key=lambda elemento: elemento[1],
    reverse=True
):

    print(region)
    print("Total:", total)
    print("Porcentaje:", porcentajes[region], "%")
    print("---"*5)