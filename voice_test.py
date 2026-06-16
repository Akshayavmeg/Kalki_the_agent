import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

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

print("Loading model...")

model = WhisperModel("base")

print("Transcribing...")

segments, info = model.transcribe("recording.wav")

for segment in segments:
    print(segment.text)