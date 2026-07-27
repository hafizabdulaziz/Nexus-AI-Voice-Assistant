"""
Action handlers for the assistant.
"""
import subprocess
import webbrowser
import os
import datetime
import pyautogui
import psutil
import requests
from .core import speak

# Weather API Key (Consider using environment variable)
WEATHER_API_KEY = "b1ae81f1cb0f2f8311efded16a82f152"

def get_weather(city):
    """Fetches weather information for a given city."""
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            speak("City not found.")
            return
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        speak(f"The temperature in {city} is {temp} degrees Celsius with {desc}")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't get the weather.")

def open_app(app_name):
    """Opens specified application."""
    try:
        app_map = {
            "whatsapp": ["start", "whatsapp"],
            "spotify": ["start", "spotify"],
            "notepad": ["notepad.exe"],
            "copilot": ["start", "copilot"],
            "calculator": ["calc.exe"]
        }
        
        if app_name in app_map:
            subprocess.Popen(app_map[app_name], shell=True)
        elif "youtube" in app_name:
            webbrowser.open("https://youtube.com")
        elif "google" in app_name:
            webbrowser.open("https://google.com")
        elif "github" in app_name:
            webbrowser.open("https://github.com")
        elif "linkedin" in app_name:
            webbrowser.open("https://linkedin.com")
        else:
            webbrowser.open(f"https://www.google.com/search?q={app_name}")
            speak(f"Searching for {app_name}")
    except Exception as e:
        print(e)
        speak("Could not open that app")

def create_file(filename):
    """Creates a new text file."""
    if "." not in filename:
        filename += ".txt"
    try:
        with open(filename, "w") as file:
            file.write("")
        speak(f"{filename} has been created.")
    except Exception as e:
        print(e)
        speak("I couldn't create this file.")

def read_file(filename):
    """Reads a text file."""
    if "." not in filename:
        filename += ".txt"
    try:
        with open(filename, "r") as file:
            content = file.read()
        if content:
            speak(content)
        else:
            speak("The file is empty.")
    except Exception as e:
        print(e)
        speak("I couldn't read this file.")

def write_file(filename, text):
    """Writes to a text file."""
    if "." not in filename:
        filename += ".txt"
    try:
        with open(filename, "a") as file:
            file.write(text + "\n")
        speak("Data has been written successfully.")
    except Exception as e:
        print(e)
        speak("I couldn't write to the file.")

def delete_file(filename):
    """Deletes a file."""
    if "." not in filename:
        filename += ".txt"
    try:
        if os.path.exists(filename):
            os.remove(filename)
            speak("File deleted successfully.")
        else:
            speak("File not found.")
    except Exception as e:
        print(e)
        speak("Couldn't delete the file.")

def open_folder(folder):
    """Opens common folders."""
    try:
        folder_map = {
            "downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
            "documents": os.path.join(os.path.expanduser("~"), "Documents"),
            "desktop": os.path.join(os.path.expanduser("~"), "Desktop")
        }
        if folder in folder_map:
            os.startfile(folder_map[folder])
        else:
            speak("Folder not found")
    except Exception as e:
        print(e)
        speak("Couldn't open folder.")

def take_screenshot():
    """Takes a screenshot."""
    try:
        filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        pyautogui.screenshot(filename)
        speak("Screenshot has been saved.")
    except Exception as e:
        print(e)
        speak("Couldn't take screenshot.")

def get_date():
    """Speaks the current date."""
    today = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today is {today}.")

def battery_status():
    """Speaks the battery status."""
    battery = psutil.sensors_battery()
    if battery:
        status = "charging" if battery.power_plugged else "not charging"
        speak(f"Battery is {battery.percent} percent and it is {status}.")
    else:
        speak("Battery information is unavailable.")

def system_info():
    """Speaks system info."""
    speak(
        f"Windows computer. "
        f"Python version is running correctly. "
        f"CPU usage is {psutil.cpu_percent()} percent."
    )

def internet_status():
    """Checks internet connectivity."""
    try:
        requests.get("https://google.com", timeout=3)
        speak("Internet is connected.")
    except:
        speak("Internet is not available.")
