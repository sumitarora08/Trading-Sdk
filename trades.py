from fastapi import APIRouter
from app.storage import trades

router = APIRouter()

@router.get("/api/v1/trades")
def get_trades():
    return trades
