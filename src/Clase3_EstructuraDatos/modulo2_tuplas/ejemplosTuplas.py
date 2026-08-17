# Primer ejemplo
coordenadas = (10, 20)
try:
    coordenadas[0] = 15
except TypeError as e:
    print(f"Error: {e}")
# 'tuple' object does not support item assignment

# Contenido mutable dentro de tupla
config = ("config_v1", [1, 2, 3])
config[1].append(4)  # OK
print(config)         # ('config_v1', [1, 2, 3, 4])

# Segundo ejemplo
# Tuplas como claves de diccionario
ubicaciones = {
    (40.7128, -74.0060): "Nueva York",
    (34.0522,-118.2437): "Los Ángeles"
}
print(ubicaciones[(40.7128, -74.0060)])  # Nueva York

# Las listas NO son hashables
try:
    d = {[40.71, -74.00]: "NY"}
except TypeError as e:
    print(f"Error: {e}")  # unhashable type: 'list'7

# Tercer ejemplo
numeros  = (1, 2, 3, 4, 5)
coords   = 10, 20, 30          # también es tupla
vacia    = ()
singleton = (42,)              # coma obligatoria

desde_lista = tuple([1, 2, 3])
desde_str   = tuple("Python")  # ('P','y','t','h','o','n')
desde_rango = tuple(range(5))  # (0, 1, 2, 3, 4)

print(type((42)))   # <class 'int'>   — SIN coma
print(type((42,)))  # <class 'tuple'> — CON coma

# Cuarto ejemplo
datos = ("Python", 3.9, 2023, "Tuplas")
print(datos[0])    # "Python"
print(datos[-1])   # "Tuplas"

nums = (0,1,2,3,4,5,6,7,8,9)
print(nums[2:6])   # (2,3,4,5)
print(nums[::2])   # (0,2,4,6,8)
print(nums[::-1])  # (9,8,7,6,5,4,3,2,1,0)

t = (1, 2, 3, 2, 4, 2, 5)
print(t.count(2))  # 3
print(t.index(3))  # 2

# Quinto ejemplo
producto = ("Laptop XPS", 1299.99, "Dell")
nombre, precio, fabricante = producto
print(nombre)      # Laptop XPS
print(precio)      # 1299.99

a, b = 5, 10
a, b = b, a        # swap en una línea
print(a, b)        # 10 5

numeros = (1, 2, 3, 4, 5)
primero, *resto          = numeros  # resto=[2,3,4,5]
primero, *medio, ultimo  = numeros  # medio=[2,3,4]
*iniciales, ultimo       = numeros  # iniciales=[1,2,3,4]

# Sexto ejemplo
datos = ("Juan","Pérez",35,"Madrid","Ingeniero")
nombre, _, edad, _, prof = datos
print(f"{nombre}, {edad}, {prof}")

estudiantes = [("Ana",22,9.5),("Carlos",20,8.7)]
for nombre, edad, nota in estudiantes:
    print(f"{nombre}: {nota}")

def estadisticas(nums):
    return min(nums), max(nums), sum(nums)/len(nums)

minima, maxima, promedio = estadisticas([4,7,2,9,5])
print(f"min={minima} max={maxima} avg={promedio:.2f}")
