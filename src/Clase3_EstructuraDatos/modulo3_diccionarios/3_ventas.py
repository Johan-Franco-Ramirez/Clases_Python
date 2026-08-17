ventas_por_region = {
    "Norte": {"Q1": 12000, "Q2": 15000, "Q3": 18000, "Q4": 16000},
    "Sur": {"Q1": 9000, "Q2": 11000, "Q3": 13000, "Q4": 14500},
    "Este": {"Q1": 14000, "Q2": 12500, "Q3": 15500, "Q4": 17000},
    "Oeste": {"Q1": 8000, "Q2": 9500, "Q3": 10000, "Q4": 12000},
}

print("=== TOTAL ANUAL POR REGIÓN ===")
totales_anuales = {}
for region, trimestres in ventas_por_region.items():
    totales_anuales[region] = sum(trimestres.values())
    print(f"{region}: {totales_anuales[region]}")

print("\n=== REGIÓN CON MAYORES VENTAS ===")
mejor_region = max(totales_anuales.items(), key=lambda item: item[1])
print(f"{mejor_region[0]} con {mejor_region[1]}")

print("\n=== VENTAS POR TRIMESTRE ===")
totales_trimestrales = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
for region, trimestres in ventas_por_region.items():
    for trimestre, monto in trimestres.items():
        totales_trimestrales[trimestre] += monto
for trimestre, total in totales_trimestrales.items():
    print(f"{trimestre}: {total}")

print("\n=== PORCENTAJES ===")
gran_total = sum(totales_anuales.values())
porcentajes = {region: total / gran_total * 100 for region, total in totales_anuales.items()}
print(f"Gran total: {gran_total}")

print("\n=== REPORTE ANUAL (mayor a menor) ===")
for region, total in sorted(totales_anuales.items(), key=lambda item: item[1], reverse=True):
    print(f"{region}: {total} ({porcentajes[region]:.1f}%)")
