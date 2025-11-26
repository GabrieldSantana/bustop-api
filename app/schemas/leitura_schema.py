# app/schemas/leitura_schema.py
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, conint, confloat


class MetaInfo(BaseModel):
    status_conforto: str


class LeituraCreate(BaseModel):
    parada_id: str = Field(..., description="ID da parada")
    device_id: Optional[str] = Field(
        default="esp32-sim-01",
        description="ID do dispositivo"
    )
    timestamp: Optional[str] = Field(
        default_factory=lambda: datetime.now().strftime("%d/%m/%Y - %H:%M"),
        description="Data e hora da leitura"
    )
    
    temperatura: confloat(ge=-50.0, le=100.0) = Field(..., description="Temperatura em °C")
    umidade: confloat(ge=0.0, le=100.0) = Field(..., description="Umidade relativa em %")
    pessoas: conint(ge=0) = Field(..., description="Número de pessoas")


    class Config:
        extra = "ignore"


class LeituraResponse(BaseModel):
    parada_id: str
    device_id: str
    timestamp: str
    temperatura: float
    umidade: float
    pessoas: int
    meta: MetaInfo