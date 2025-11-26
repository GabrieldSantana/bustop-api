from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List

from ..deps import get_database
from ..schemas.leitura_schema import LeituraCreate, LeituraResponse
from ..services import leitura_service

router = APIRouter()


@router.post("/api/dados", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_leitura(
    leitura: LeituraCreate, db=Depends(get_database)
):
    try:
        inserted_id = await leitura_service.save_leitura(db, leitura)
        return inserted_id
        # return {
        #     "message": "Dados recebidos e salvos no MongoDB!",
        #     "id": inserted_id
        # }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@router.get("/api/dados", response_model=List[LeituraResponse])
async def get_leituras(
    limit: int = Query(100, gt=0, le=1000),
    db=Depends(get_database)
):
    try:
        docs = await leitura_service.list_leituras(db, limit)

        # Converter ObjectId para string se existir
        for d in docs:
            if "_id" in d:
                d["id"] = str(d["_id"])
                del d["_id"]

        return docs
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))