from core.router import route
from core.risk import evaluate

def execute(plan: dict):

    risk = evaluate(plan)

    if not risk["approved"]:
        return {
            "status": "blocked",
            "reason": risk["reason"]
        }

    return route(plan)
