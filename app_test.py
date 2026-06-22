import subprocess

apps = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe"
}

app_name = input("Enter app name: ").lower()

if app_name in apps:
    subprocess.Popen(apps[app_name])
    print(f"Opening {app_name}")
else:
    print("App not found")