# Gym Microservice - Python (FastAPI)

Microservicio REST de **ejercicios, rutinas y comidas** conectado a la **misma base de datos Supabase** que el microservicio original. Expone el mismo contrato de API (mismos métodos, rutas y campos) para ser intercambiable con los microservicios en Java, Node y Go.

## Stack

- Python 3.10+ + FastAPI
- Cliente HTTP `httpx` hacia Supabase REST (PostgREST)
- Swagger UI nativo en `/docs`
- CORS habilitado globalmente

## Requisitos

- Python 3.10 o superior

## Configuración

Copia `.env.example` a `.env` y coloca las credenciales (mismas que el proyecto original):

```env
SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_KEY=tu_key_de_supabase
PORT=8001
```

> Se usa el puerto `8001` porque el `8000` lo ocupa el proyecto Django "Gym Tracker".

## Levantar

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux / macOS
pip install -r requirements.txt
python -m app.main
```

O con uvicorn directamente:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8001
```

## Probar desde Swagger

- Swagger UI: http://localhost:8001/docs
- OpenAPI JSON: http://localhost:8001/openapi.json
- ReDoc: http://localhost:8001/redoc

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/` | Info de la API |
| GET | `/ejercicios` | Listar ejercicios |
| GET | `/ejercicios/{id}` | Obtener un ejercicio |
| POST | `/ejercicios` | Crear ejercicio |
| PUT | `/ejercicios/{id}` | Actualizar ejercicio |
| DELETE | `/ejercicios/{id}` | Eliminar ejercicio |
| GET | `/rutinas` | Listar rutinas |
| GET | `/rutinas/{id}` | Obtener rutina con sus ejercicios |
| POST | `/rutinas` | Crear rutina |
| PUT | `/rutinas/{id}` | Actualizar rutina |
| DELETE | `/rutinas/{id}` | Eliminar rutina |
| GET | `/comidas` | Listar comidas |
| GET | `/comidas/{id}` | Obtener comida |
| POST | `/comidas` | Crear comida |
| PUT | `/comidas/{id}` | Actualizar comida |
| DELETE | `/comidas/{id}` | Eliminar comida |
