from fastapi import FastAPI
from backend.tools.wallet import create_wallet
from backend.tools.balance import get_balance

app = FastAPI(title="MCP Wallet Tools")

@app.get("/tools")
def tools():
    return {
        "tools": [
            "create_wallet",
            "get_balance"
        ]
    }

@app.post("/tool/create_wallet")
def tool_create():
    return create_wallet()

@app.post("/tool/balance")
def tool_balance(data: dict):
    return get_balance(data["address"])
