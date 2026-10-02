from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import PORT
from app.routers import comidas, ejercicios, rutinas
from app.supabase_client import ApiError

app = FastAPI(
    title="Gym Microservice - Python (FastAPI)",
    version="1.0.0",
    description=(
        "API de ejercicios, rutinas y comidas conectada a Supabase via REST. "
        "Mismo contrato que los microservicios en Java, Node y Go."
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(ApiError)
async def api_error_handler(request: Request, exc: ApiError):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.message})


app.include_router(ejercicios.router)
app.include_router(rutinas.router)
app.include_router(comidas.router)


@app.get("/", tags=["Root"], summary="Informacion de la API y endpoints disponibles")
async def root():
    return {
        "mensaje": "API Gym Microservice",
        "endpoints": {
            "ejercicios": "/ejercicios",
            "rutinas": "/rutinas",
            "comidas": "/comidas",
        },
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=PORT)
