from faster_whisper import WhisperModel
from ollama import chat

import sounddevice as sd
from scipy.io.wavfile import write

import subprocess
import pyautogui
import time
import json
import webbrowser

# Supported Apps
apps = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vs code": r"C:\Users\aksha\AppData\Local\Programs\Microsoft VS Code\Code.exe"
}

SYSTEM_PROMPT = """
You are an AI desktop agent.

Allowed actions ONLY:

open
open_and_type
calculate
search

Never invent new actions.
Always use one of the allowed actions.


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
User: Open Chrome and search AI agents

Output:
{"app":"chrome","action":"search","query":"AI agents"}
User: Open VS Code and write a Python hello world program

Output:
{"app":"vs code","action":"open_and_type","text":"print('Hello World')"}

User: Open VS Code and write a Python for loop from 1 to 10

Output:
{"app":"vs code","action":"open_and_type","text":"for i in range(1,11):\n    print(i)"}
Return ONLY JSON.
"""

# -----------------------
# Record Voice
# -----------------------

duration = 5
sample_rate = 16000

print("Speak now...")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="int16"
)

sd.wait()

write("recording.wav", sample_rate, audio)

print("Transcribing...")

# -----------------------
# Whisper
# -----------------------

model = WhisperModel("base")

segments, info = model.transcribe("recording.wav")

command = ""

for segment in segments:
    command += segment.text

command = command.lower().strip()

print("Heard:", command)

# -----------------------
# Ollama
# -----------------------

response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": command
        }
    ]
)

result = response["message"]["content"]

print("\nLLM Output:")
print(result)

# -----------------------
# Parse JSON
# -----------------------

try:
    data = json.loads(result)

except Exception as e:
    print("JSON Error:", e)
    exit()

app = data.get("app")
action = data.get("action")

if app not in apps:
    print("Unsupported app:", app)
    exit()

# -----------------------
# Execute Action
# -----------------------

if action != "search":
    subprocess.Popen(apps[app])

print("Opening:", app)
if action == "open_and_type":

    text = data.get("text", "")

    if app == "vs code":

        time.sleep(5)

        pyautogui.click(500, 500)

        time.sleep(1)

        pyautogui.hotkey("ctrl", "n")

        time.sleep(1)

    else:

        time.sleep(2)

    pyautogui.write(text, interval=0.05)

    print("Typed:", text)

    pyautogui.write(text, interval=0.05)

    print("Typed:", text)

    expression = data.get("expression", "")

    time.sleep(2)

    pyautogui.write(expression)

    pyautogui.press("enter")

    print("Calculated:", expression)

if "search" in action:

    query = data.get("query", "")

    subprocess.Popen([
        apps["chrome"],
        f"https://www.google.com/search?q={query}"
    ])

    print("Searching:", query)