import requests

def swap_token(data: dict):
    """
    Placeholder for 1inch / Uniswap router
    """

    return {
        "status": "simulated",
        "from": data["token_in"],
        "to": data["token_out"],
        "amount": data["amount"],
        "route": "best_path_mock"
    }
