from fastapi import FastAPI
from tools.wallet import create_wallet
from tools.balance import get_balance
from tools.send import send_eth
from tools.history import tx_history

app = FastAPI(title="Agent Wallet OS")

wallet_db = {}  # MVP in-memory storage

@app.get("/")
def home():
    return {"status": "Agent Wallet Running"}

@app.post("/wallet/create")
def wallet_create():
    wallet = create_wallet()
    wallet_db[wallet["address"]] = wallet
    return wallet

@app.get("/wallet/balance/{address}")
def balance(address: str):
    return get_balance(address)

@app.post("/wallet/send")
def send(payload: dict):
    return send_eth(payload)

@app.get("/wallet/history/{address}")
def history(address: str):
    return tx_history(address)
