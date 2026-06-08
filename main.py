from fastapi import FastAPI
from tools.wallet import create_wallet

app = FastAPI(title="Agent Wallet")

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/wallet/create")
def wallet_create():
    return create_wallet()
