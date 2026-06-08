import requests

BASE = "http://localhost:8000"

def run_agent(prompt: str):
    prompt = prompt.lower()

    if "create wallet" in prompt:
        return requests.post(f"{BASE}/wallet/create").json()

    if "balance" in prompt:
        address = prompt.split()[-1]
        return requests.get(f"{BASE}/wallet/balance/{address}").json()

    return {"error": "unknown command"}
