import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

import subprocess
import pyautogui
import time

# Record audio
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

print("Heard exactly:", repr(command))

# Command parsing
if "type" in command:

    text = command.split("type", 1)[1].strip()

    subprocess.Popen("notepad.exe")

    time.sleep(2)

    pyautogui.write(text, interval=0.05)

else:
    print("Command not recognized")