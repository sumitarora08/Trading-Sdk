from fastapi import FastAPI
from app.routes.instruments import router as instruments_router
from app.routes.orders import router as orders_router
from app.routes.trades import router as trades_router
from app.routes.portfolio import router as portfolio_router

app = FastAPI(title="Trading SDK")

app.include_router(instruments_router)
app.include_router(orders_router)
app.include_router(trades_router)
app.include_router(portfolio_router)

@app.get("/")
def home():
    return {"message": "Trading API is running"}
