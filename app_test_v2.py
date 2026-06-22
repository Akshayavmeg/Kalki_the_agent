import subprocess

apps = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vs code": r"C:\Users\aksha\AppData\Local\Programs\Microsoft VS Code\Code.exe"
}

app_name = input("App name: ").lower()

if app_name in apps:
    subprocess.Popen(apps[app_name])
    print(f"Opening {app_name}")
else:
    print("App not found")