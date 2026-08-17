# prestamos_equipos.py
from datetime import datetime

# Estructura principal de datos (Diccionario anidado)
# Clave: Nombre del equipo
# Valor: Diccionario con 'disponible' (bool) y 'prestamos' (lista de tuplas)
inventario_equipos = {
    "Laptop HP": {
        "disponible": True,
        "prestamos": []
    },
    "Proyector Epson": {
        "disponible": True,
        "prestamos": []
    },
    "Tablet Lenovo": {
        "disponible": False,
        "prestamos": [("Carlos Gómez", "2026-06-10 14:30")]
    }
}


def mostrar_equipos():
    """
    Muestra en pantalla todos los equipos registrados en el sistema
    y su estado actual (disponible o prestado).
    """
    print("\n--- INVENTARIO DE EQUIPOS ---")
    if not inventario_equipos:
        print("No hay equipos registrados en el sistema.")
        return

    for equipo, datos in inventario_equipos.items():
        estado = "Disponible" if datos["disponible"] else "Prestado"
        print(f"* Equipo: {equipo} | Estado: {estado}")
    print("-" * 29)


def registrar_prestamo():
    """
    Permite registrar un nuevo préstamo de un equipo validando su existencia
    y disponibilidad, guardando la tupla (usuario, fecha).
    """
    print("\n--- REGISTRAR PRÉSTAMO ---")
    mostrar_equipos()
    
    if not inventario_equipos:
        return

    equipo = input("Ingrese el nombre exacto del equipo a prestar: ").strip()

    # Validar que el equipo exista
    if equipo not in inventario_equipos:
        print(f"Error: El equipo '{equipo}' no existe en el sistema.")
        return

    # Validar que el equipo esté disponible
    if not inventario_equipos[equipo]["disponible"]:
        print(f"Error: El equipo '{equipo}' ya se encuentra prestado.")
        return

    usuario = input("Ingrese el nombre del usuario que hace el préstamo: ").strip()
    if not usuario:
        print("Error: El nombre del usuario no puede estar vacío.")
        return

    # Generar la fecha actual en formato de cadena (para guardar en la tupla)
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Guardar los datos en una tupla inmutable (usuario, fecha) y añadirla a la lista
    prestamo_tupla = (usuario, fecha_actual)
    inventario_equipos[equipo]["prestamos"].append(prestamo_tupla)

    # Cambiar el estado del equipo a no disponible
    inventario_equipos[equipo]["disponible"] = False

    print(f"¡Éxito! Préstamo registrado correctamente para '{usuario}' con el equipo '{equipo}'.")


def devolver_equipo():
    """
    Permite marcar un equipo como devuelto cambiando su estado a disponible.
    """
    print("\n--- DEVOLVER EQUIPO ---")
    if not inventario_equipos:
        print("No hay equipos en el sistema.")
        return

    equipo = input("Ingrese el nombre exacto del equipo a devolver: ").strip()

    # Validar que el equipo exista
    if equipo not in inventario_equipos:
        print(f"Error: El equipo '{equipo}' no existe en el sistema.")
        return

    # Validar que el equipo esté actualmente prestado
    if inventario_equipos[equipo]["disponible"]:
        print(f"Error: El equipo '{equipo}' ya se encontraba disponible (no estaba prestado).")
        return

    # Cambiar su estado a disponible nuevamente
    inventario_equipos[equipo]["disponible"] = True
    print(f"¡Éxito! El equipo '{equipo}' ha sido devuelto y ahora está disponible.")


def ver_historial():
    """
    Muestra el historial completo de préstamos registrados en el sistema por cada equipo.
    """
    print("\n--- HISTORIAL COMPLETO DE PRÉSTAMOS ---")
    if not inventario_equipos:
        print("No hay equipos registrados en el sistema.")
        return

    for equipo, datos in inventario_equipos.items():
        print(f"\nEquipo: {equipo}")
        prestamos = datos["prestamos"]
        if prestamos:
            print("  Historial de préstamos:")
            for i, (usuario, fecha) in enumerate(prestamos, start=1):
                print(f"    {i}. Usuario: {usuario} | Fecha: {fecha}")
        else:
            print("  Sin préstamos registrados.")
    print("-" * 40)


def agregar_equipo():
    """
    Permite agregar nuevos equipos al sistema verificando que no existan previamente.
    """
    print("\n--- AGREGAR NUEVO EQUIPO ---")
    nuevo_equipo = input("Ingrese el nombre del nuevo equipo: ").strip()

    if not nuevo_equipo:
        print("Error: El nombre del equipo no puede estar vacío.")
        return

    # Verificar que el equipo no exista ya en el diccionario
    if nuevo_equipo in inventario_equipos:
        print(f"Error: El equipo '{nuevo_equipo}' ya existe en el inventario.")
        return

    # Agregar al inventario con estado disponible = True y lista de préstamos vacía
    inventario_equipos[nuevo_equipo] = {
        "disponible": True,
        "prestamos": []
    }

    print(f"¡Éxito! El equipo '{nuevo_equipo}' se ha agregado correctamente al sistema.")


def menu():
    """
    Ofrece un menú interactivo que permite al usuario elegir entre las operaciones
    principales del sistema de forma repetitiva hasta que decida salir.
    """
    while True:
        print("\n========================================")
        print("   SISTEMA DE PRÉSTAMOS DE EQUIPOS      ")
        print("========================================")
        print("1. Ver equipos disponibles")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial de préstamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir del programa")
        print("========================================")

        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            print("\n¡Gracias por usar el Sistema de Préstamos de Equipos! Saliendo...")
            break
        else:
            print("\nOpción inválida. Por favor, ingrese un número entre 1 y 6.")


if __name__ == "__main__":
    menu()