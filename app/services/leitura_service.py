from typing import List
from motor.motor_asyncio import AsyncIOMotorDatabase

from ..repositories import leitura_repository as repo
from ..schemas.leitura_schema import LeituraCreate
from datetime import datetime


def calcular_status_conforto(temp: float, umid: float) -> str:
    if 20 <= temp <= 26 and 30 <= umid <= 60:
        return "confortável"
    return "desconfortável"


async def save_leitura(db: AsyncIOMotorDatabase, leitura_in: LeituraCreate) -> str:
    # meta
    status = calcular_status_conforto(leitura_in.temperatura, leitura_in.umidade)
    meta = {"status_conforto": status}

    # salvar no Mongo
    await repo.insert_leitura(
        db=db,
        parada_id=leitura_in.parada_id,
        device_id=leitura_in.device_id,
        temperatura=leitura_in.temperatura,
        umidade=leitura_in.umidade,
        pessoas=leitura_in.pessoas,
        timestamp=leitura_in.timestamp,
        meta=meta,
    )

    return {
        "parada_id": leitura_in.parada_id,
        "device_id": leitura_in.device_id,
        "timestamp": leitura_in.timestamp,
        "temperatura": leitura_in.temperatura,
        "umidade": leitura_in.umidade,
        "pessoas": leitura_in.pessoas,
        "meta": meta
    }


async def list_leituras(db: AsyncIOMotorDatabase, limit: int = 100) -> List[dict]:
    return await repo.get_leituras(db, limit)