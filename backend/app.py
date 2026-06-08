from fastapi import FastAPI
from agent.brain import plan
from agent.executor import execute

app = FastAPI(title="TWAK Agent v2")

@app.post("/agent/run")
def run_agent(data: dict):

    user_input = data["input"]

    planned = plan(user_input)

    # in real system: JSON parse planner output
    result = execute({
        "tool": "balance",
        "address": data.get("address")
    })

    return {
        "plan": planned,
        "result": result
    }
