from fastapi import APIRouter
from app.storage import portfolio, instruments

router = APIRouter()

@router.get("/api/v1/portfolio")
def get_portfolio():
    response = []

    for symbol, data in portfolio.items():
        # get latest market price
        ltp = next(
            i["lastTradedPrice"] for i in instruments if i["symbol"] == symbol
        )

        response.append({
            "symbol": symbol,
            "quantity": data["quantity"],
            "averagePrice": round(data["averagePrice"], 2),
            "currentValue": round(data["quantity"] * ltp, 2)
        })

    return response
