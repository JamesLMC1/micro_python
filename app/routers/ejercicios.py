from typing import Optional

from fastapi import APIRouter

from app.schemas import Ejercicio, EjercicioRequest, MensajeResponse
from app.supabase_client import ApiError, supabase

router = APIRouter(prefix="/ejercicios", tags=["Ejercicios"])


@router.get("", response_model=list[Ejercicio], summary="Listar todos los ejercicios")
async def listar():
    return await supabase.select("ejercicios", {"select": "*"})


@router.get("/{id}", response_model=Ejercicio, summary="Obtener un ejercicio por id")
async def obtener(id: str):
    rows = await supabase.select("ejercicios", {"select": "*", "id": f"eq.{id}"})
    if not rows:
        raise ApiError(404, "Ejercicio no encontrado")
    return rows[0]


@router.post("", response_model=Ejercicio, status_code=201, summary="Crear un ejercicio")
async def crear(req: EjercicioRequest):
    rows = await supabase.insert("ejercicios", req.model_dump(exclude_none=True))
    return rows[0] if rows else None


@router.put("/{id}", response_model=Optional[Ejercicio], summary="Actualizar un ejercicio")
async def actualizar(id: str, req: EjercicioRequest):
    rows = await supabase.update("ejercicios", id, req.model_dump(exclude_none=True))
    return rows[0] if rows else None


@router.delete("/{id}", response_model=MensajeResponse, summary="Eliminar un ejercicio")
async def eliminar(id: str):
    await supabase.delete("ejercicios", id)
    return {"mensaje": "Ejercicio eliminado"}
