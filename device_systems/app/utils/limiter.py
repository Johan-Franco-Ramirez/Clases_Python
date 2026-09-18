from slowapi import Limiter
from slowapi.util import get_remote_address

# Inicializa el limitador usando la dirección IP del cliente como clave de identificación
limiter = Limiter(key_func=get_remote_address)