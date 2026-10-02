from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class MensajeResponse(BaseModel):
    mensaje: str


class ErrorResponse(BaseModel):
    error: str


class EjercicioRequest(BaseModel):
    nombre: Optional[str] = None
    grupo_muscular: Optional[str] = None
    descripcion: Optional[str] = None
    dificultad: Optional[str] = None
    imagen_url: Optional[str] = None


class Ejercicio(BaseModel):
    id: UUID
    nombre: str
    grupo_muscular: str
    descripcion: Optional[str] = None
    dificultad: Optional[str] = None
    imagen_url: Optional[str] = None
    created_at: Optional[datetime] = None


class RutinaRequest(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    nivel: Optional[str] = None
    duracion_dias: Optional[int] = None


class Rutina(BaseModel):
    id: UUID
    nombre: str
    descripcion: Optional[str] = None
    nivel: Optional[str] = None
    duracion_dias: Optional[int] = None
    created_at: Optional[datetime] = None


class RutinaEjercicio(BaseModel):
    id: UUID
    rutina_id: Optional[UUID] = None
    ejercicio_id: Optional[UUID] = None
    series: Optional[int] = None
    repeticiones: Optional[str] = None
    descanso_segundos: Optional[int] = None
    ejercicios: Optional[Ejercicio] = None


class RutinaDetalle(Rutina):
    ejercicios: list[RutinaEjercicio] = []


class ComidaRequest(BaseModel):
    nombre: Optional[str] = None
    tipo: Optional[str] = None
    calorias: Optional[int] = None
    proteinas_g: Optional[float] = None
    carbos_g: Optional[float] = None
    grasas_g: Optional[float] = None
    receta: Optional[str] = None


class Comida(BaseModel):
    id: UUID
    nombre: str
    tipo: Optional[str] = None
    calorias: Optional[int] = None
    proteinas_g: Optional[float] = None
    carbos_g: Optional[float] = None
    grasas_g: Optional[float] = None
    receta: Optional[str] = None
    created_at: Optional[datetime] = None
