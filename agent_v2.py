import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

import subprocess
import pyautogui
import time

# Supported Apps
apps = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe"
}

# Record Audio
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

model = WhisperModel("base")

segments, info = model.transcribe("recording.wav")

command = ""

for segment in segments:
    command += segment.text

command = command.lower()

print("Heard:", command)

# Detect App
selected_app = None

for app in apps:
    if app in command:
        selected_app = app
        break

if selected_app:

    subprocess.Popen(apps[selected_app])

    print(f"Opening {selected_app}")

    if "type" in command:

        text = command.split("type", 1)[1].strip()

        time.sleep(2)

        pyautogui.write(text, interval=0.05)

else:
    print("No supported app found")