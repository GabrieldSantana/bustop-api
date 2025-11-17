# app/routes/leitura_router.py
from fastapi import APIRouter
from ..controllers.leitura_controller import router as leitura_router

router = APIRouter()
router.include_router(leitura_router)