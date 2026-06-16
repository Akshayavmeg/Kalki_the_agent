command = input("Say a command: ")

command = command.lower()

if "open notepad and type" in command:
    text = command.replace("open notepad and type", "").strip()

    print("App:", "notepad")
    print("Text:", text)

else:
    print("Command not recognized")