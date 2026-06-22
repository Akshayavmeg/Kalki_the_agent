from ollama import chat

SYSTEM_PROMPT = """
You are an AI agent.

Return ONLY a JSON object.

Examples:

User: Open VS Code and type hello world

Output:
{"app":"vs code","action":"open_and_type","text":"hello world"}

User: Open calculator

Output:
{"app":"calculator","action":"open"}

Do not explain anything.
Return only JSON.
"""

response = chat(
    model="llama3.2:3b",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Open VS Code and type hello world"}
    ]
)

print(response["message"]["content"])