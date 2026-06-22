from ollama import chat

response = chat(
    model='llama3.2:3b',
    messages=[
        {
            'role': 'user',
            'content': 'Open VS Code and type hello world'
        }
    ]
)

print(response['message']['content'])