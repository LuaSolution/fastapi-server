from fastapi import APIRouter
from starlette.responses import JSONResponse
from typing import Optional

router = APIRouter()

@router.get("/items/{item_id}")
def read_item(item_id: int):
    return JSONResponse({"item_id": item_id})
