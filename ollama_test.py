from ollama import chat

SYSTEM_PROMPT = """
You are an AI desktop agent.

Return ONLY valid JSON.

Examples:

User: Open calculator

Output:
{"app":"calculator","action":"open"}

User: Calculate 567 times 89

Output:
{"app":"calculator","action":"calculate","expression":"567*89"}

User: Calculate 100 plus 200

Output:
{"app":"calculator","action":"calculate","expression":"100+200"}

User: Open Chrome

Output:
{"app":"chrome","action":"open"}

User: Open Chrome and search AI agents

Output:
{"app":"chrome","action":"search","query":"AI agents"}

User: Open VS Code and type hello world

Output:
{"app":"vs code","action":"open_and_type","text":"hello world"}

User: Open notepad and type hello world

Output:
{"app":"notepad","action":"open_and_type","text":"hello world"}

Return ONLY JSON.
"""

response = chat(
    model="llama3.2:3b",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":"Calculate 456 times 789"}
    ]
)

print(response["message"]["content"])