#validacion del nombre
def validar_nombre(nombre):
    if not nombre:
        return False

    if not nombre.strip():
        return False

    return True

#validacion del correo
def validar_correo(correo):
    if not correo:
        return False

    correo = correo.strip()

    if "@" not in correo:
        return False

    if "." not in correo:
        return False

    return True

#validacion de la contraseña
def validar_contrasena(contrasena):
    if not contrasena:
        return False

    if len(contrasena) < 6:
        return False

    return True

#