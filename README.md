# Trading-Sdk
Developed a simplified trading backend using FastAPI that simulates core stock broking workflows. Implemented REST APIs for instruments, order placement, order tracking, trade execution, and portfolio management using in-memory storage, with Swagger-based API documentation and validation.

**#PROJECT DESCRIPTION**
This project implements a mock trading backend system that simulates essential workflows of an online stock broking platform. It exposes RESTful APIs to view instruments, place orders, track order status, view executed trades, and fetch portfolio holdings. The system uses in-memory storage and is designed for clarity, correctness, and easy extensibility.

**#SCHEMA**
trading-sdk/
│
├── app/
│   ├── main.py              # Application entry point
│   ├── models.py            # Request/response data models
│   ├── storage.py           # In-memory data storage
│   └── routes/
│       ├── instruments.py   # Instrument APIs
│       ├── orders.py        # Order management APIs
│       ├── trades.py        # Trade APIs
│       └── portfolio.py     # Portfolio APIs
│
├── requirements.txt
└── README.md

**Data Schema (In-Memory)
Instrument**
{
  "symbol": "RELIANCE",
  "exchange": "NSE",
  "instrumentType": "EQ",
  "lastTradedPrice": 2500
}

**Order**
{
  "orderId": 1,
  "symbol": "RELIANCE",
  "orderType": "BUY",
  "orderStyle": "MARKET",
  "quantity": 5,
  "price": null,
  "status": "EXECUTED"
}
**Trade**
{
  "orderId": 1,
  "symbol": "RELIANCE",
  "quantity": 5,
  "price": 2500
}

**Portfolio Holding**
{
  "symbol": "RELIANCE",
  "quantity": 5,
  "averagePrice": 2500,
  "currentValue": 12500
}

**API Flow (High-Level)**
User fetches available instruments
User places a BUY/SELL order
MARKET orders are executed immediately
Executed orders generate trades
Trades update portfolio holdings
User can query orders, trades, and portfolio at any time

**Key Design Decisions**
Single mocked user (no authentication)
MARKET orders execute instantly
LIMIT orders are validated and stored
In-memory storage for simplicity
RESTful API design with proper HTTP status codes
Auto-generated Swagger documentation

**API DOCUMENTATION-**
Swagger UI is available at 
http://localhost:8000/docs

**Error Handling**
The system validates inputs and returns meaningful errors for:
Invalid quantity
Missing price for LIMIT order
Invalid instrument symbols
Invalid order IDs



