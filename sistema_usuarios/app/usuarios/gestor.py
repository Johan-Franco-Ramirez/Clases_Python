# Importar las funciones de validación
from app.usuarios.validaciones import (
    validar_nombre,
    validar_correo,
    validar_contrasena
)


# Clase encargada de gestionar los usuarios
class GestorUsuarios:

    # Inicializar la lista de usuarios
    def __init__(self):
        self.usuarios = []

    # Registrar un nuevo usuario
    def registrar_usuario(self, nombre, correo, contrasena):

        # Validación del nombre
        if not validar_nombre(nombre):
            return "El nombre no es válido."

        # Validación del correo
        if not validar_correo(correo):
            return "El correo no es válido."

        # Validación de la contraseña
        if not validar_contrasena(contrasena):
            return "La contraseña debe tener mínimo 6 caracteres."

        # Comprobar que el correo no esté registrado
        if self.buscar_usuario(correo) is not None:
            return "Ya existe un usuario con ese correo."

        # Crear el diccionario del usuario
        usuario = {
            "nombre": nombre.strip(),
            "correo": correo.strip().lower(),
            "contrasena": contrasena
        }

        # Agregar el usuario a la lista
        self.usuarios.append(usuario)

        return "Usuario registrado correctamente."

    # Listar todos los usuarios
    def listar_usuarios(self):
        return self.usuarios

    # Buscar un usuario por correo
    def buscar_usuario(self, correo):

        # Recorrer la lista de usuarios
        for usuario in self.usuarios:

            # Comparar los correos sin importar mayúsculas
            if usuario["correo"].lower() == correo.strip().lower():
                return usuario

        # Retornar None si no se encuentra el usuario
        return None

    # Actualizar los datos de un usuario
    def actualizar_usuario(self, correo, nuevo_nombre, nueva_contrasena):

        # Buscar el usuario
        usuario = self.buscar_usuario(correo)

        if usuario is None:
            return "Usuario no encontrado."

        # Validar el nuevo nombre
        if not validar_nombre(nuevo_nombre):
            return "El nombre no es válido."

        # Validar la nueva contraseña
        if not validar_contrasena(nueva_contrasena):
            return "La contraseña debe tener mínimo 6 caracteres."

        # Actualizar los datos
        usuario["nombre"] = nuevo_nombre.strip()
        usuario["contrasena"] = nueva_contrasena

        return "Usuario actualizado correctamente."

    # Eliminar un usuario
    def eliminar_usuario(self, correo):

        # Buscar el usuario
        usuario = self.buscar_usuario(correo)

        if usuario is None:
            return "Usuario no encontrado."

        # Eliminar el usuario de la lista
        self.usuarios.remove(usuario)

        return "Usuario eliminado correctamente."