Proyecto device_systems
---

# 🚀 device_systems API

Aplicación backend desarrollada con **FastAPI** para construir una API REST enfocada en la gestión del recurso de usuarios, aplicando validaciones, parámetros de ruta/consulta, response models y cabeceras HTTP personalizadas.

---

## 📋 Descripción de la aplicación
`device_systems` es un sistema backend optimizado para administrar de forma limpia y estructurada los perfiles de los usuarios del sistema. Implementa buenas prácticas de desarrollo en capas y control de errores HTTP.

---

## ⚙️ Instalación de dependencias
Sigue estos pasos para clonar el proyecto y configurar el entorno virtual:


2. **Crear y activar el entorno virtual:**
```bash
python -m venv .venv
source .venv/Scripts/activate  # En Windows (Git Bash / Linux)
# O si usas PowerShell: .\.venv\Scripts\Activate

```


3. **Instalar las dependencias:**
```bash
pip install fastapi uvicorn pydantic email-validator

```



---

## 🏃‍♂️ Ejecución del servidor

Para iniciar el servidor de desarrollo con recarga automática, ejecuta:

```bash
python -m uvicorn app.main:app --reload

```

El servidor se ejecutará localmente en: `http://127.0.0.1:8000`

La documentación interactiva (**Swagger UI**) estará disponible en: `http://127.0.0.1:8000/docs`

---

## 📌 Tabla de Endpoints

| Método | Endpoint | Descripción | Parámetros / Query Params |
| --- | --- | --- | --- |
| **GET** | `/users` | Lista todos los usuarios o filtra por rol y estado. | `role` (admin, support, user), `is_active` (bool) |
| **GET** | `/users/{user_id}` | Consulta un usuario específico por su ID único. | `user_id` (Path Parameter) |
| **POST** | `/users` | Registra un nuevo usuario validando datos y correos duplicados. | Body JSON (`UserCreate`) |

---

## 🧪 Ejemplos de Peticiones y Pruebas

### 1. Registrar un usuario (`POST /users`)

* **URL:** `http://127.0.0.1:8000/users`
* **Body (JSON):**
```json
{
  "name": "Mateo Giraldo",
  "email": "mateo@example.com",
  "role": "admin",
  "is_active": true
}

```


* **Respuesta Esperada (`201 Created`):**
```json
{
  "name": "Mateo Giraldo",
  "email": "mateo@example.com",
  "role": "admin",
  "is_active": true,
  "id": 4
}

```



### 2. Consultar usuarios filtrados (`GET /users?role=admin`)

* **URL:** `http://127.0.0.1:8000/users?role=admin`
* **Respuesta Esperada (`200 OK`):** Devuelve la lista filtrada con las cabeceras personalizadas:
* `X-App-Name: device_systems`
* `X-API-Version: 1.0`

---

## 💡 Reflexión sobre el uso de FastAPI

El uso de FastAPI para este desarrollo facilita enormemente la construcción de APIs REST gracias a su tipado estricto con Python y la validación automática de esquemas mediante Pydantic v2. Esto reduce la cantidad de código repetitivo de validación manual, previene errores en tiempo de ejecución y genera de forma automática una documentación interactiva sumamente útil para realizar pruebas rápidas y eficientes durante el ciclo de vida del desarrollo.

---
## Johan Franco R. ADSO.
