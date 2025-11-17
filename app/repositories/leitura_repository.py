# app/repositories/leitura_repository.py
from typing import List
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId

COLLECTION = "leituras"


async def insert_leitura(
    db: AsyncIOMotorDatabase, temperatura: float, umidade: float, pessoas: int
) -> str:
    doc = {
        "temperatura": float(temperatura),
        "umidade": float(umidade),
        "pessoas": int(pessoas),
        "timestamp": datetime.utcnow(),
    }
    result = await db[COLLECTION].insert_one(doc)
    return str(result.inserted_id)


async def get_leituras(db: AsyncIOMotorDatabase, limit: int = 100) -> List[dict]:
    cursor = db[COLLECTION].find().sort("timestamp", -1).limit(limit)
    docs = []
    async for doc in cursor:
        doc["id"] = str(doc.get("_id") or "")
        doc.pop("_id", None)
        docs.append(doc)
    return docs
