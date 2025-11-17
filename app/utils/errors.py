# app/utils/errors.py
from fastapi import HTTPException, status


def bad_request(detail: str = "Dados inválidos"):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)