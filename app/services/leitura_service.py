# app/services/leitura_service.py
from typing import List
from motor.motor_asyncio import AsyncIOMotorDatabase

from ..repositories import leitura_repository as repo
from ..schemas.leitura_schema import LeituraCreate


async def save_leitura(db: AsyncIOMotorDatabase, leitura_in: LeituraCreate) -> str:
    # Aqui mantemos validação por Pydantic + regras extra se precisar.
    # Se houver regras de negócio adicionais, aplique-as aqui.
    inserted_id = await repo.insert_leitura(
        db, leitura_in.temperatura, leitura_in.umidade, leitura_in.pessoas
    )
    return inserted_id


async def list_leituras(db: AsyncIOMotorDatabase, limit: int = 100) -> List[dict]:
    return await repo.get_leituras(db, limit)
