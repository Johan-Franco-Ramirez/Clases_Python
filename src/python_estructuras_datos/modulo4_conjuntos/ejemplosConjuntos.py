#1
colores = {"rojo","verde","azul","rojo"}
print(colores)  # {'verde','azul','rojo'} — sin "rojo" duplicado

numeros = set([1, 2, 3, 2, 1])
print(numeros)  # {1, 2, 3}

# Búsqueda eficiente
frutas = {"manzana","naranja","plátano"}
print("manzana" in frutas)  # True — O(1)

# Conjunto vacío
vacio = set()
print(type({}))   # <class 'dict'>   — NO es un set
print(type(set())) # <class 'set'>   — correcto

#2
tecnologias = {"Python","JavaScript","SQL"}
tecnologias.add("Java")
tecnologias.update(["Go","Rust"])

frutas = {"manzana","naranja","platano"}
frutas.remove("naranja")    # OK
frutas.discard("kiwi")      # silencioso — kiwi no existe
elem = frutas.pop()         # aleatorio
frutas.clear()              # set()

# issubset / issuperset
pares = {2,4,6,8}
nums  = {1,2,3,4,5,6,7,8,9}
print(pares.issubset(nums))   # True
print(nums.issuperset(pares)) # True

#3
grupo_a = {"Ana","Carlos","Elena","David"}
grupo_b = {"Carlos","Elena","Fernando"}

comunes     = grupo_a.intersection(grupo_b)  # {'Carlos','Elena'}
todos       = grupo_a.union(grupo_b)
solo_en_a   = grupo_a.difference(grupo_b)    # {'Ana','David'}
exclusivos  = grupo_a.symmetric_difference(grupo_b)

vegetales = {"zanahoria","pepino"}
frutas    = {"manzana","platano"}
print(vegetales.isdisjoint(frutas))  # True — sin elementos comunes

# Encadenamiento
resultado = grupo_a.intersection(grupo_b).difference({"Elena"})
# → {'Carlos'}

#4
u1 = {"acción","comedia","ciencia ficción","aventura"}
u2 = {"drama","comedia","romance","documental"}
u3 = {"acción","aventura","fantasía","ciencia ficción"}

comunes_1_3  = u1 & u3   # {'acción','ciencia ficción','aventura'}
todos_1_2    = u1 | u2
solo_u1      = u1 - u2   # excluye lo de u2
excl_2_3     = u2 ^ u3   # en uno pero no en ambos

# Operadores de comparación
print(u3 <= u1)  # False — u3 NO es subconjunto de u1
print({2,4} <= {1,2,3,4,5})  # True