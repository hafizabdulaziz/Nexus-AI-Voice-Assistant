"""
Core functionality, configuration, and data management for Nexus.
"""
import json
import os
import ollama
import pyttsx3

# Configuration
USER_FILE = "user_data.json"
VOICE_RATE = 195
VOICE_VOLUME = 1.0
ASSISTANT_NAME = "Nexus"

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty("rate", VOICE_RATE)
engine.setProperty("volume", VOICE_VOLUME)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# Global State
user_name = ""
user_notes = []
conversation_history = []

def speak(text):
    """Speaks the given text."""
    print(f"{ASSISTANT_NAME}: {text}")
    engine.say(text)
    engine.runAndWait()

def load_user_data():
    """Loads user data from JSON file."""
    global user_name, user_notes, conversation_history
    try:
        if os.path.exists(USER_FILE):
            with open(USER_FILE, "r") as file:
                data = json.load(file)
                user_name = data.get("name", "")
                user_notes = data.get("notes", [])
                conversation_history = data.get("history", [])
                if user_name:
                    speak(f"Welcome back {user_name}.")
    except Exception as e:
        print(f"Error loading data: {e}")
        user_name = ""
        user_notes = []
        conversation_history = []

def save_user_data():
    """Saves user data to JSON file."""
    data = {
        "name": user_name,
        "notes": user_notes,
        "history": conversation_history
    }
    with open(USER_FILE, "w") as file:
        json.dump(data, file, indent=4)

def get_ai_reply(prompt):
    """Gets a reply from the Ollama AI model."""
    try:
        if user_name:
            prompt = f"The user's name is {user_name}. Address them by their name naturally.\nUser: {prompt}"
        
        system_prompt = f"""
        You are {ASSISTANT_NAME}, a Windows voice assistant.
        Rules:
        - Your name is {ASSISTANT_NAME}.
        - Never refuse normal questions.
        - Answer every general knowledge question.
        - Maximum 20 words.
        - One sentence only.
        - Never say you cannot answer.
        - Never mention policies.
        - Be friendly and direct.
        """
        
        conversation_history.append({"role": "user", "content": f"{system_prompt}\n{prompt}"})
        
        response = ollama.chat(
            model="llama3.2:latest",
            messages=conversation_history
        )
        reply = response["message"]["content"].replace("\n", " ").strip()
        
        conversation_history.append({"role": "assistant", "content": reply})
        
        # Keep history manageable
        MAX_HISTORY = 4
        if len(conversation_history) > MAX_HISTORY:
            conversation_history[:] = conversation_history[-MAX_HISTORY:]
            
        save_user_data()
        return reply
    except Exception as e:
        print(f"DEBUG Ollama Error: {e}")
        return "I'm having trouble thinking right now."
