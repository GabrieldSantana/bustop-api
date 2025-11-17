# app/controllers/leitura_controller.py
from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List

from ..deps import get_database
from ..schemas.leitura_schema import LeituraCreate, LeituraInDB
from ..services import leitura_service

router = APIRouter()


@router.post("/api/dados", status_code=status.HTTP_201_CREATED)
async def create_leitura(
    leitura: LeituraCreate, db=Depends(get_database)
) -> dict:
    try:
        inserted_id = await leitura_service.save_leitura(db, leitura)
        return {"message": "Dados recebidos e salvos no MongoDB!", "id": inserted_id}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/api/dados", response_model=List[LeituraInDB])
async def get_leituras(limit: int = Query(100, gt=0, le=1000), db=Depends(get_database)):
    try:
        docs = await leitura_service.list_leituras(db, limit)
        # Conversão mínima para o schema (pydantic) será automática
        return docs
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
