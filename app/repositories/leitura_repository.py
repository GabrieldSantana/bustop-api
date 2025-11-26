from typing import List
from motor.motor_asyncio import AsyncIOMotorDatabase
from datetime import datetime

COLLECTION = "leituras"


async def insert_leitura(
    db: AsyncIOMotorDatabase,
    parada_id: str,
    device_id: str,
    temperatura: float,
    umidade: float,
    pessoas: int,
    timestamp: str,
    meta: dict
) -> str:
    """
    Insere uma leitura completa no MongoDB
    """
    doc = {
        "parada_id": parada_id,
        "device_id": device_id,
        "temperatura": float(temperatura),
        "umidade": float(umidade),
        "pessoas": int(pessoas),
        "timestamp": timestamp,
        "meta": meta,
    }
    result = await db[COLLECTION].insert_one(doc)
    return str(result.inserted_id)


async def get_leituras(db: AsyncIOMotorDatabase, limit: int = 100) -> List[dict]:
    """
    Retorna as últimas leituras do MongoDB, já formatando id e mantendo campos extras
    """
    cursor = db[COLLECTION].find().sort("timestamp", -1).limit(limit)
    docs = []
    async for doc in cursor:
        # Converte _id para id
        doc["id"] = str(doc.get("_id") or "")
        doc.pop("_id", None)

        # Garantir campos obrigatórios no retorno
        doc.setdefault("parada_id", "")
        doc.setdefault("device_id", "esp32-sim-01")
        doc.setdefault("meta", {"status_conforto": "desconhecido"})

        docs.append(doc)
    return docs