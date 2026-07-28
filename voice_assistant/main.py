"""
Main entry point for Nexus voice assistant.
"""
import datetime
from .core import (
    speak, load_user_data, save_user_data, get_ai_reply, 
    ASSISTANT_NAME, user_name, user_notes
)
from .utils import listen
from . import actions

waiting_for_city = False

def greet():
    """Greets the user on startup."""
    speak(f"{ASSISTANT_NAME} is ready.")
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

def main():
    """Main execution loop."""
    global user_name, waiting_for_city
    greet()
    load_user_data()
    speak(f"This is {ASSISTANT_NAME}, your personal assistant.")
    speak("Ready. How Can I Help You?")

    while True:
        command = listen()
        if not command:
            continue
        
        # Assistant name handler
        if ASSISTANT_NAME.lower() in command:
            command = command.replace(ASSISTANT_NAME.lower(), "").strip()
            if not command:
               speak("Yes?")
               continue
        
        # Command routing
        if "hello" in command:
           speak("Hello How are You?")
        elif "thank you" in command or "thanks" in command:
            speak("You're Welcome.")
        elif "time" in command:
           speak(f"The time is {datetime.datetime.now().strftime('%I:%M %p')}")
        elif "date" in command:
            actions.get_date()
        elif "battery" in command:
            actions.battery_status()
        elif "system info" in command:
            actions.system_info()
        elif "internet" in command:
            actions.internet_status()
        elif "my name is" in command:
           user_name = command.replace("my name is", "").strip()
           save_user_data()
           speak(f"Nice to meet you, {user_name}. I will remember your name.")
        elif "remember that" in command:
            note = command.replace("remember that", "").strip()
            user_notes.append(note)
            save_user_data()
            speak("Okay, I will remember that.")
        elif "show my notes" in command:
            for note in user_notes: speak(note) if user_notes else speak("No notes.")
        elif "forget my notes" in command:
            user_notes.clear()
            save_user_data()
            speak("All your notes have been deleted.")
        elif "open" in command:
            target = command.replace("open", "").strip()
            if any(f in target for f in ["downloads", "documents", "desktop"]):
                actions.open_folder(target)
            else:
                actions.open_app(target)
        elif "search" in command:
            query = command.replace("search", "").strip()
            actions.open_app(query)
        elif "weather" in command or "temperature" in command:
            city = command.split()[-1]
            actions.get_weather(city)
        elif "create file" in command:
            actions.create_file(command.replace("create file", "").strip())
        elif "read file" in command:
            actions.read_file(command.replace("read file", "").strip())
        elif "write file" in command:
            # Simple handling: "write file <filename> <content>"
            # This is hard to parse reliably without a better approach.
            # I will just perform a basic implementation.
            parts = command.replace("write file", "").strip().split(" ", 1)
            if len(parts) == 2:
                actions.write_file(parts[0], parts[1])
            else:
                speak("Please specify filename and content.")
        elif "delete file" in command:
            actions.delete_file(command.replace("delete file", "").strip())
        elif "screenshot" in command:
            actions.take_screenshot()
        elif "goodbye" in command or "exit" in command:
           speak("Goodbye.")
           break
        else:
           reply = get_ai_reply(command)
           speak(reply)

if __name__ == "__main__":
    main()
