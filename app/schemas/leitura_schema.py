# app/schemas/leitura_schema.py
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, conint, confloat


class LeituraCreate(BaseModel):
    temperatura: confloat(ge=-50.0, le=100.0) = Field(..., description="Temperatura em °C")
    umidade: confloat(ge=0.0, le=100.0) = Field(..., description="Umidade relativa em %")
    pessoas: conint(ge=0) = Field(..., description="Número de pessoas")


class LeituraInDB(BaseModel):
    id: Optional[str]
    temperatura: float
    umidade: float
    pessoas: int
    timestamp: datetime

    class Config:
        orm_mode = True
