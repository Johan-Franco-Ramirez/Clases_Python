# Importar herramientas para trabajar con variables de entorno
import os

# Importar la función para cargar el archivo .env
from dotenv import load_dotenv


# Cargar las variables del archivo .env
load_dotenv()


# Obtener el nombre de la aplicación
APP_NAME = os.getenv("APP_NAME", "Sistema de Usuarios")


# Obtener y convertir el modo DEBUG a un valor booleano
DEBUG = os.getenv("DEBUG", "False").lower() == "true"