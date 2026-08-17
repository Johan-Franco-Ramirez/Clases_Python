# Primer ejemplo
# Bucle tradicional
cuadrados = []
for n in range(10):
    cuadrados.append(n**2)

# List comprehension — equivalente más conciso
cuadrados = [n**2 for n in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Con filtro
pares = [n for n in range(10) if n%2 == 0]
# [0, 2, 4, 6, 8]

# Transformación + extracción
celsius = [0, 10, 20, 30, 40]
fahr = [(9/5)*t + 32 for t in celsius]

usuarios = [{"nombre":"Ana","edad":28},{"nombre":"Carlos","edad":35}]
nombres = [u["nombre"] for u in usuarios]  # ['Ana','Carlos']

# Segundo ejemplo
# Cuadrados
cuadrados = {n: n**2 for n in range(5)}
# {0:0, 1:1, 2:4, 3:9, 4:16}

# Filtrar stock disponible
stock = {"manzanas":10,"platanos":3,"naranjas":25,"peras":0}
disponibles = {f:c for f,c in stock.items() if c > 0}

# Invertir diccionario
original  = {"a":1, "b":2, "c":3}
invertido = {v:k for k,v in original.items()}  # {1:"a", 2:"b", 3:"c"}

# Desde lista de dicts
estudiantes = [{"id":1,"nombre":"Ana"},{"id":2,"nombre":"Carlos"}]
id_nombre = {e["id"]: e["nombre"] for e in estudiantes}

# Tercer ejemplo
# Eliminar duplicados con transformación
numeros = [1,2,2,3,4,3,5,5,1]
unicos  = {n for n in numeros}  # {1,2,3,4,5}

# Iniciales únicas
palabras   = ["manzana","banana","mango","mora","naranja"]
iniciales  = {p[0] for p in palabras}  # {'m','b','n'}

# Vocales únicas en un texto
texto  = "python es un lenguaje versátil"
vocales = {l for l in texto.lower() if l in "aeiou"}

# Filtro: cuadrados de pares únicos
pares_cuad = {n**2 for n in range(10) if n%2==0}
# {0, 4, 16, 36, 64}7

# Cuarto ejemplo
ventas = [
    {"producto":"laptop",  "unidades":20, "precio":800},
    {"producto":"teclado", "unidades":50, "precio":25},
    {"producto":"mouse",   "unidades":30, "precio":15},
    {"producto":"monitor", "unidades":10, "precio":200}
]
# List comp: valor total por producto
valor_por_producto = [i["unidades"]*i["precio"] for i in ventas]
# [16000, 1250, 450, 2000]

# List comp con filtro: alto valor
alto_valor = [i["producto"] for i in ventas
              if i["unidades"]*i["precio"] > 1000]
# ['laptop','teclado','monitor']

# Dict comp: nombre → valor total
resumen = {i["producto"]: i["unidades"]*i["precio"] for i in ventas}

# Gran total
gran_total = sum(valor_por_producto)  # 19700

# Quinto ejemplo
# Comprehension simple — legible y eficiente
cuadrados = [n**2 for n in range(100)]

# Generador para colecciones grandes — ahorra memoria
gen = (n**2 for n in range(1_000_000))
primero = next(gen)  # solo calcula uno a la vez

# Cuándo usar bucle tradicional — lógica compleja
resultados = []
for item in datos: # type: ignore
    if item["activo"]:
        valor = calcular(item)
        if valor > umbral:
            resultados.append(transformar(valor))
# Esta lógica es más clara en bucle que en comprehension

