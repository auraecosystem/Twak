from tools.wallet import create_wallet
from tools.balance import get_balance
from tools.send import send_eth
from defi.swap import swap_token

def route(action: dict):
    tool = action.get("tool")

    if tool == "create_wallet":
        return create_wallet()

    if tool == "balance":
        return get_balance(action["address"])

    if tool == "send":
        return send_eth(action)

    if tool == "swap":
        return swap_token(action)

    return {"error": "unknown tool"}
