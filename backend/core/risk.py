def evaluate(tx: dict):
    amount = float(tx.get("amount", 0))

    if amount > 1:
        return {
            "approved": False,
            "reason": "High value transaction requires manual approval"
        }

    if tx.get("to") is None:
        return {
            "approved": False,
            "reason": "Missing recipient"
        }

    return {
        "approved": True,
        "risk": "low"
    }
