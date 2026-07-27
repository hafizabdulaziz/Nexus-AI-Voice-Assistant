"""
Voice listening utility.
"""
import speech_recognition as sr
from .core import speak

def listen():
    """Listens for user voice input."""
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 70
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 1.0
    recognizer.non_speaking_duration = 0.5
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
           audio = recognizer.listen(
               source,
               timeout=10,
               phrase_time_limit=10
            )
           command = recognizer.recognize_google(audio, language="en-US")
           print(f"You Said : {command}")
           return command.lower()
        except sr.UnknownValueError:
           speak("Sorry I didn't Catch That.")
           return ""
        except sr.RequestError:
           speak("Network Error.")
           return ""
        except Exception as e:
            print(f"Listening error: {e}")
            return ""
