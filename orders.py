from fastapi import APIRouter, HTTPException
from app.models import OrderRequest, OrderResponse
from app.storage import orders, trades, portfolio, instruments

router = APIRouter()

order_counter = 1

@router.post("/api/v1/orders", response_model=OrderResponse)
def place_order(order: OrderRequest):
    global order_counter

    # Basic validations
    if order.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0")

    if order.orderStyle == "LIMIT" and order.price is None:
        raise HTTPException(status_code=400, detail="Price is required for LIMIT orders")

    # Check if instrument exists
    symbols = [i["symbol"] for i in instruments]
    if order.symbol not in symbols:
        raise HTTPException(status_code=404, detail="Instrument not found")

    order_id = order_counter
    order_counter += 1

    # Default status
    status = "PLACED"

    # MARKET orders execute immediately
    if order.orderStyle == "MARKET":
        status = "EXECUTED"

        # Get market price
        market_price = next(
            i["lastTradedPrice"] for i in instruments if i["symbol"] == order.symbol
        )

        # Save trade
        trades.append({
            "orderId": order_id,
            "symbol": order.symbol,
            "quantity": order.quantity,
            "price": market_price
        })

        # Update portfolio
        if order.symbol not in portfolio:
            portfolio[order.symbol] = {
                "quantity": 0,
                "averagePrice": market_price
            }

        total_qty = portfolio[order.symbol]["quantity"] + order.quantity
        portfolio[order.symbol]["averagePrice"] = (
            (portfolio[order.symbol]["averagePrice"] * portfolio[order.symbol]["quantity"]
             + market_price * order.quantity) / total_qty
        )

        portfolio[order.symbol]["quantity"] = total_qty

    # Save order
    orders[order_id] = {
        "orderId": order_id,
        "symbol": order.symbol,
        "orderType": order.orderType,
        "orderStyle": order.orderStyle,
        "quantity": order.quantity,
        "price": order.price,
        "status": status
    }

    return {"orderId": order_id, "status": status}
@router.get("/api/v1/orders/{order_id}")
def get_order_status(order_id: int):
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="Order not found")

    return orders[order_id]
