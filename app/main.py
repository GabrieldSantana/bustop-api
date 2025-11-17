# app/main.py
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from .config import settings
from .routes.leitura_router import router as leitura_router
from .deps import get_client

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("bustop_api")

app = FastAPI(title="BuStop API", version="1.0.0", description="API migrada de Express -> FastAPI")

# CORS (imitando comportamento do server.js)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


@app.get("/", tags=["health"])
def root() -> dict:
    return {"message": "API BuStop está rodando!"}


app.include_router(leitura_router)


@app.on_event("startup")
async def startup_event():
    # inicialize cliente se desejar testar conexão
    try:
        client = get_client()
        # opcional: testar ping (sincrono não-blocking: motor é lazy)
        logger.info("FastAPI startup complete, Mongo client created.")
    except Exception as exc:
        logger.exception("Erro ao conectar com MongoDB: %s", exc)


@app.on_event("shutdown")
async def shutdown_event():
    try:
        client = get_client()
        client.close()
        logger.info("Mongo client fechado.")
    except Exception:
        pass


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.API_PORT, reload=True)
