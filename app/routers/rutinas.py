from typing import Optional

from fastapi import APIRouter

from app.schemas import MensajeResponse, Rutina, RutinaDetalle, RutinaRequest
from app.supabase_client import ApiError, supabase

router = APIRouter(prefix="/rutinas", tags=["Rutinas"])


@router.get("", response_model=list[Rutina], summary="Listar todas las rutinas")
async def listar():
    return await supabase.select("rutinas", {"select": "*"})


@router.get("/{id}", response_model=RutinaDetalle, summary="Obtener una rutina con sus ejercicios")
async def obtener(id: str):
    rows = await supabase.select("rutinas", {"select": "*", "id": f"eq.{id}"})
    if not rows:
        raise ApiError(404, "Rutina no encontrada")
    ejercicios = await supabase.select(
        "rutina_ejercicios", {"select": "*,ejercicios(*)", "rutina_id": f"eq.{id}"}
    )
    return {**rows[0], "ejercicios": ejercicios}


@router.post("", response_model=Rutina, status_code=201, summary="Crear una rutina")
async def crear(req: RutinaRequest):
    rows = await supabase.insert("rutinas", req.model_dump(exclude_none=True))
    return rows[0] if rows else None


@router.put("/{id}", response_model=Optional[Rutina], summary="Actualizar una rutina")
async def actualizar(id: str, req: RutinaRequest):
    rows = await supabase.update("rutinas", id, req.model_dump(exclude_none=True))
    return rows[0] if rows else None


@router.delete("/{id}", response_model=MensajeResponse, summary="Eliminar una rutina")
async def eliminar(id: str):
    await supabase.delete("rutinas", id)
    return {"mensaje": "Rutina eliminada"}
