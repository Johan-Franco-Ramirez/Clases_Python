# device_systems API - Seguridad y Autenticación
GA1-220501096-01-AA1-EV11 – FastAPI Seguridad: Autenticación, Middleware, CORS, Rate Limiting y Validación Avanzada.

## 📌 Descripción del Proyecto
Evolución de la API REST **device_systems** para incorporar una capa de seguridad profesional. El sistema gestiona usuarios, dispositivos tecnológicos y préstamos, integrando autenticación basada en **OAuth2 con JWT**, cifrado seguro de contraseñas con **Passlib (bcrypt)**, control de acceso basado en roles (`admin`, `support`, `user`), validaciones robustas con **Pydantic v2**, middleware de trazabilidad, control de tráfico con **Rate Limiting** y configuración estricta de **CORS**.

---

## 🗂️ Estructura del Proyecto
```text
device_systems/
├── app/
│   ├── main.py
│   ├── auth/
│   │   ├── auth_routes.py
│   │   ├── auth_service.py
│   │   └── security.py
│   ├── database/
│   │   └── connection.py
│   ├── models/
│   │   ├── user_model.py
│   │   ├── device_model.py
│   │   └── loan_model.py
│   ├── schemas/
│   │   ├── user_schema.py
│   │   ├── device_schema.py
│   │   ├── loan_schema.py
│   │   └── auth_schema.py
│   ├── routes/
│   │   ├── user_routes.py
│   │   ├── device_routes.py
│   │   └── loan_routes.py
│   ├── services/
│   │   ├── user_service.py
│   │   ├── device_service.py
│   │   └── loan_service.py
│   ├── dependencies/
│   │   ├── database_dependency.py
│   │   └── auth_dependency.py
│   ├── middlewares/
│   │   └── request_middleware.py
│   └── utils/
│       └── limiter.py
├── alembic/
│   └── versions/
├── .env
├── .env.example
├── alembic.ini
├── requirements.txt
└── README.md
(Insertar aquí captura de la estructura del proyecto en VS Code)

⚙️ Configuración y Ejecución del Entorno
Cambiar a la rama de seguridad en Git:

Bash
git checkout device_systems_security
Instalar dependencias necesarias:

Bash
pip install -r requirements.txt
Configurar el archivo de variables de entorno (.env):
Copia el archivo .env.example como .env y define los parámetros de tu base de datos y la llave secreta para los tokens JWT (SECRET_KEY).

Aplicar la migración de Alembic para los campos de seguridad:

Bash
alembic upgrade head
(Insertar aquí captura de la consola ejecutando la migración de Alembic)

Iniciar el servidor local con Uvicorn:

Bash
uvicorn app.main:app --reload
🔒 Características de Seguridad Implementadas
Hash de Contraseñas: Uso de passlib con algoritmo bcrypt para garantizar que las credenciales nunca se almacenen ni expongan en texto plano.

Autenticación OAuth2 & JWT: Emisión de tokens de acceso firmados para validar sesiones de usuario de forma segura.

Control de Acceso por Roles (RBAC): Restricción de endpoints basada en los perfiles admin, support y user.

Validaciones Avanzadas: Reglas estrictas en Pydantic v2 (longitud mínima de 8 caracteres, inclusión de mayúsculas, minúsculas, números y restricción de espacios en blanco).

🌐 Configuración de CORS
En el archivo main.py se implementó CORSMiddleware restringiendo los orígenes permitidos a los clientes de desarrollo autorizados:

http://localhost:5173

http://localhost:3000

¿Por qué no se recomienda usar "*" en producción con credenciales?
Utilizar un comodín allow_origins=["*"] en conjunto con allow_credentials=True introduce un riesgo crítico de seguridad. Los navegadores modernos bloquean automáticamente peticiones con credenciales (como tokens Bearer) si el servidor acepta cualquier origen de forma indiscriminada, evitando que sitios web maliciosos secuestren sesiones activas de los usuarios.

📸 Evidencias de Pruebas Funcionales
Registro de Usuario Válido:

(Insertar captura de pantalla del registro exitoso en Swagger/Postman)

Registro con Contraseña Débil (Validación Pydantic):

(Insertar captura del error 422 Unprocessable Entity)

Login y Generación de Token JWT:

(Insertar captura del endpoint /auth/login retornando el access_token)

Consulta de Perfil Protegido (/auth/me):

(Insertar captura de la respuesta con los datos del usuario sin exponer hashed_password)

Acceso sin Token a Ruta Protegida:

(Insertar captura de la respuesta HTTP 401 Unauthorized)

Acceso con Rol No Permitido:

(Insertar captura de la respuesta HTTP 403 Forbidden al intentar ejecutar una acción exclusiva de admin)

Documentación Swagger / OpenAPI con OAuth2:

(Insertar captura de Swagger UI mostrando los candados de seguridad)

Cabeceras del Middleware Personalizado:

(Insertar captura de las headers X-App-Name, X-Process-Time y X-Request-ID)

Activación de Rate Limiting:

(Insertar captura de la respuesta HTTP 429 Too Many Requests tras superar el límite de peticiones)

💡 Reflexión Final
La incorporación de mecanismos avanzados de seguridad en una API REST representa un estándar indispensable en el desarrollo de software moderno. El uso de autenticación basada en tokens JWT, cifrado seguro con bcrypt, control estricto de roles y limitación de tráfico protege de manera integral los datos del sistema frente a ataques informáticos comunes como la fuerza bruta o la suplantación de identidad, preparando la aplicación para despliegues reales en entornos de producción empresariales.