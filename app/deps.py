# app/deps.py
from typing import AsyncGenerator

from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings

_client: AsyncIOMotorClient | None = None


def get_client() -> AsyncIOMotorClient:
    global _client
    if _client is None:
        _client = AsyncIOMotorClient(settings.MONGO_URI)
    return _client


async def get_database() -> AsyncGenerator:
    client = get_client()
    db = client[settings.MONGO_DB]
    try:
        yield db
    finally:
        # Não fechamos client aqui para reaproveitar conexões; cleanup no shutdown se desejar
        pass
