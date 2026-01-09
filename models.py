from pydantic import BaseModel
from typing import Optional

class OrderRequest(BaseModel):
    symbol: str
    orderType: str        # BUY / SELL
    orderStyle: str       # MARKET / LIMIT
    quantity: int
    price: Optional[float] = None


class OrderResponse(BaseModel):
    orderId: int
    status: str
