from openai import OpenAI

client = OpenAI()

SYSTEM_PROMPT = """
You are a blockchain execution agent.

You do NOT execute directly.
You ONLY:
1. Understand intent
2. Create structured plan
3. Call tools via router

Rules:
- Never send funds without approval flag
- Always validate risk level
- Prefer low-risk routes
"""

def plan(user_input: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content
