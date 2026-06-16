import subprocess
import pyautogui
import time

# Open Notepad
subprocess.Popen("notepad.exe")

# Wait for Notepad to open
time.sleep(2)

# Type text
pyautogui.write("Hello from my AI Agent!", interval=0.05)