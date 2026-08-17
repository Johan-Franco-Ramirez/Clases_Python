# Importar el gestor de usuarios
from app.usuarios.gestor import GestorUsuarios


# Crear el gestor de usuarios
gestor = GestorUsuarios()


# Mostrar las opciones disponibles
def mostrar_menu():
    print("\n================================")
    print("      SISTEMA DE USUARIOS")
    print("================================")
    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Actualizar usuario")
    print("5. Eliminar usuario")
    print("6. Salir")
    print("================================")


# Ciclo principal del programa
while True:

    # Mostrar el menú
    mostrar_menu()

    # Solicitar una opción al usuario
    opcion = input("Seleccione una opción: ")

    # Registrar un nuevo usuario
    if opcion == "1":

        nombre = input("Ingrese el nombre: ")
        correo = input("Ingrese el correo: ")
        contrasena = input("Ingrese la contraseña: ")

        resultado = gestor.registrar_usuario(
            nombre,
            correo,
            contrasena
        )

        print(resultado)

    # Listar todos los usuarios
    elif opcion == "2":

        usuarios = gestor.listar_usuarios()

        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            print("\nUsuarios registrados:")

            for usuario in usuarios:
                print(f"Nombre: {usuario['nombre']}")
                print(f"Correo: {usuario['correo']}")
                print("-" * 30)

    # Buscar un usuario por correo
    elif opcion == "3":

        correo = input("Ingrese el correo a buscar: ")

        usuario = gestor.buscar_usuario(correo)

        if usuario:
            print("\nUsuario encontrado:")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Correo: {usuario['correo']}")
        else:
            print("Usuario no encontrado.")

    # Actualizar los datos de un usuario
    elif opcion == "4":

        correo = input("Ingrese el correo del usuario: ")
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nueva_contrasena = input("Ingrese la nueva contraseña: ")

        resultado = gestor.actualizar_usuario(
            correo,
            nuevo_nombre,
            nueva_contrasena
        )

        print(resultado)

    # Eliminar un usuario
    elif opcion == "5":

        correo = input("Ingrese el correo del usuario: ")

        resultado = gestor.eliminar_usuario(correo)

        print(resultado)

    # Salir del programa
    elif opcion == "6":

        print("Gracias por utilizar el sistema.")
        break

    # Manejar una opción inexistente
    else:
        print("Opción no válida. Intente nuevamente.")
