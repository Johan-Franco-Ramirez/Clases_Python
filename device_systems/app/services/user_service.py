from app.data.users_db import users_db

def get_all_users():
    # Obtener todos los usuarios de la lista
    return users_db

def get_user_by_id(user_id: int):
    # Buscar usuario por ID o retornar None
    for user in users_db:
        if user["id"] == user_id:
            return user
    return None

def create_user(user_data: dict):
    # Crear usuario con ID autoincremental
    new_id = max([user["id"] for user in users_db], default=0) + 1
    new_user = {"id": new_id, **user_data}
    users_db.append(new_user)
    return new_user

def update_user(user_id: int, user_data: dict):
    # Actualizar datos de un usuario existente preservando su ID
    user = get_user_by_id(user_id)
    if user is None:
        return None

    user.update(user_data)
    return user