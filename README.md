# 🛒 FastAPI Ecommerce Project 🛒

¡Bienvenido/a al proyecto **FastAPI Ecommerce**! Este repositorio contiene una API construida con **FastAPI** que permite gestionar pedidos de un sistema de comercio electrónico. A continuación, encontrarás toda la información necesaria para configurar y ejecutar el proyecto.

---

## 📦 Dependencias del Proyecto

Antes de comenzar, asegúrate de tener instaladas las siguientes dependencias:

- **Python 3.12** 🐍
- **FastAPI** ⚡
- **Uvicorn** 🌐 (Servidor ASGI)
- **SQLAlchemy** 🗄️ (ORM para manejo de bases de datos)
- **AsyncMy** 🔄 (Driver asíncrono para MySQL)

### Instalación de dependencias

Para instalar las dependencias, puedes usar `pipenv`:

```bash
pipenv install
```

---

## 📂 Estructura del Proyecto

```
└── feliprado31-fastapi_ecommerce/
    ├── Pipfile                🔧 Archivo de dependencias
    ├── database.py            🗄️ Configuración de la base de datos
    ├── extensions.py          🛠️ Extensiones adicionales (Flask-SQLAlchemy)
    ├── main.py                🚀 Aplicación principal de FastAPI
    ├── models.py              🏗️ Definición de modelos de la base de datos
    └── schemas.py             📝 Esquemas Pydantic para validación de datos
```

---

## 🌟 Funcionalidades del Proyecto

Este proyecto proporciona una API RESTful para gestionar pedidos en un sistema de comercio electrónico. A continuación, se describen las principales funcionalidades:

### 📅 Endpoint: Obtener Pedidos por Rango de Fechas

- **URL**: `/pedidos/`
- **Método**: `GET`
- **Parámetros**:
  - `fecha_inicial` (requerido): Fecha inicial en formato `YYYY-MM-DD`.
  - `fecha_final` (requerido): Fecha final en formato `YYYY-MM-DD`.

#### Respuesta

La respuesta incluye una lista de pedidos realizados dentro del rango de fechas especificado, con detalles sobre los productos comprados y el total del pedido.

Ejemplo de respuesta:

```json
[
  {
    "id_pedido": 1,
    "fecha_creacion": "2023-10-01 14:30:00",
    "estado": "pendiente",
    "productos": [
      {
        "nombre": "Laptop",
        "precio_unitario": 1500.0,
        "cantidad": 1,
        "total_producto": 1500.0
      },
      {
        "nombre": "Mouse",
        "precio_unitario": 25.0,
        "cantidad": 2,
        "total_producto": 50.0
      }
    ],
    "total_pedido": 1550.0
  }
]
```

---

## 🛠️ Configuración de la Base de Datos

El proyecto utiliza **MySQL** como base de datos. Asegúrate de configurar la conexión en el archivo `database.py`:

```python
DATABASE_URL = "mysql+asyncmy://root:root@localhost/ecommerce"
```

### Pasos para configurar la base de datos:

1. Crea una base de datos llamada `ecommerce` en tu servidor MySQL.
2. Actualiza las credenciales en `DATABASE_URL` si es necesario.
3. Ejecuta las migraciones para crear las tablas correspondientes.

---

## ▶️ Ejecución del Proyecto

Una vez configuradas las dependencias y la base de datos, puedes ejecutar el proyecto con el siguiente comando:

```bash
uvicorn main:app --reload
```

- La API estará disponible en: `http://127.0.0.1:8000`
- Documentación interactiva (Swagger UI): `http://127.0.0.1:8000/docs`

---

## 📜 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.


---

Made with ❤️ by [feliprado31](https://github.com/feliprado31)