from typing import Optional

from fastapi import APIRouter

from app.schemas import Comida, ComidaRequest, MensajeResponse
from app.supabase_client import ApiError, supabase

router = APIRouter(prefix="/comidas", tags=["Comidas"])


@router.get("", response_model=list[Comida], summary="Listar todas las comidas")
async def listar():
    return await supabase.select("comidas", {"select": "*"})


@router.get("/{id}", response_model=Comida, summary="Obtener una comida por id")
async def obtener(id: str):
    rows = await supabase.select("comidas", {"select": "*", "id": f"eq.{id}"})
    if not rows:
        raise ApiError(404, "Comida no encontrada")
    return rows[0]


@router.post("", response_model=Comida, status_code=201, summary="Crear una comida")
async def crear(req: ComidaRequest):
    rows = await supabase.insert("comidas", req.model_dump(exclude_none=True))
    return rows[0] if rows else None


@router.put("/{id}", response_model=Optional[Comida], summary="Actualizar una comida")
async def actualizar(id: str, req: ComidaRequest):
    rows = await supabase.update("comidas", id, req.model_dump(exclude_none=True))
    return rows[0] if rows else None


@router.delete("/{id}", response_model=MensajeResponse, summary="Eliminar una comida")
async def eliminar(id: str):
    await supabase.delete("comidas", id)
    return {"mensaje": "Comida eliminada"}
