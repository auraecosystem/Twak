from fastapi import FastAPI
from core.router import route

app = FastAPI(title="TWAK MCP Server")

@app.post("/invoke")
def invoke(data: dict):
    return route(data)
