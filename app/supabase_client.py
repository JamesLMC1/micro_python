from typing import Any

import httpx

from app.config import REST_URL, SUPABASE_KEY


class ApiError(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(message)


def _error_message(response: httpx.Response) -> str:
    try:
        data = response.json()
        if isinstance(data, dict) and data.get("message"):
            return data["message"]
    except Exception:
        pass
    return response.text or "Error en Supabase"


class SupabaseRest:
    """Cliente minimo para la API REST de Supabase (PostgREST)."""

    def __init__(self) -> None:
        self.headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
        }

    async def select(self, table: str, params: dict[str, str] | None = None) -> list[dict[str, Any]]:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(
                f"{REST_URL}/{table}", params=params or {}, headers=self.headers
            )
        if response.status_code >= 400:
            raise ApiError(500, _error_message(response))
        return response.json()

    async def insert(self, table: str, body: dict[str, Any]) -> list[dict[str, Any]]:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                f"{REST_URL}/{table}",
                json=body,
                headers={**self.headers, "Prefer": "return=representation"},
            )
        if response.status_code >= 400:
            raise ApiError(400, _error_message(response))
        return response.json()

    async def update(self, table: str, item_id: str, body: dict[str, Any]) -> list[dict[str, Any]]:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.patch(
                f"{REST_URL}/{table}",
                params={"id": f"eq.{item_id}"},
                json=body,
                headers={**self.headers, "Prefer": "return=representation"},
            )
        if response.status_code >= 400:
            raise ApiError(400, _error_message(response))
        return response.json()

    async def delete(self, table: str, item_id: str) -> None:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.delete(
                f"{REST_URL}/{table}",
                params={"id": f"eq.{item_id}"},
                headers=self.headers,
            )
        if response.status_code >= 400:
            raise ApiError(400, _error_message(response))


supabase = SupabaseRest()
