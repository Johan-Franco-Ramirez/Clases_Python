# Primer ejemplo
contactos = {
    "Ana":    "612345678",
    "Carlos": "698765432"
}
print(contactos["Ana"])                    # 612345678
print(contactos.get("Elena", "No encontrado"))  # No encontrado

# Claves válidas (inmutables)
valido = {"nombre":"Juan", 42:"respuesta", (1,2):"coord"}

# INVÁLIDAS
# invalido = {[1,2]: "x"}  # TypeError: unhashable type: 'list'

# Segundo ejemplo
colores = dict(rojo="#FF0000", verde="#00FF00", azul="#0000FF")

claves  = ["nombre", "edad", "ciudad"]
valores = ["Ana", 28, "Madrid"]
persona = {k: v for k, v in zip(claves, valores)}

# Diccionario anidado
usuario = {
    "nombre": "Miguel", "edad": 30,
    "direccion": {"calle":"Calle Mayor","ciudad":"Madrid"}
}
ciudad = usuario["direccion"]["ciudad"]  # "Madrid"

# Tercer ejemplo
califs = {"Mates": 85, "Historia": 72}
califs.update({"Inglés": 88, "Mates": 87, "Arte": 95})

vendido = califs.pop("Inglés")      # retorna 88
par_final = califs.popitem()        # último par insertado

contador = {}
contador.setdefault("hola", 0)
contador["hola"] += 1               # → {"hola": 1}

materias = ["Mates","Historia","Arte"]
notas = dict.fromkeys(materias, 0)  # → {"Mates":0, ...}

d1 = {"nombre":"Carlos","edad":28}
d2 = {"email":"c@e.com"}
unido = d1 | d2                     # fusión Python 3.9+

# Cuarto ejemplo
califs = {"Mates":85, "Historia":72, "Ciencias":90}

for asig, nota in califs.items():
    print(f"{asig}: {nota}")

# Orden alfabético de claves
for asig in sorted(califs):
    print(f"{asig}: {califs[asig]}")

# Iteración segura: eliminar mientras recorres
d = {"a":1, "b":2, "c":3}
for k in list(d.keys()):
    if k == "b": del d[k]   # OK — iterando copia
print(d)  # {"a":1, "c":3}

# Quinto ejemplo
precios = {"laptop":899, "tablet":349}

# Aplicar descuento del 10%
rebaja = {p: round(v*0.9, 2) for p,v in precios.items()}

# Filtrar productos disponibles
stock = {"manzanas":10, "peras":0, "naranjas":25}
disponibles = {f:c for f,c in stock.items() if c > 0}

# Invertir clave-valor
original  = {"a":1, "b":2, "c":3}
invertido = {v:k for k,v in original.items()}

# Porcentaje del total
gran_total = sum(precios.values())
pct = {p: round(v/gran_total*100,1) for p,v in precios.items()}

