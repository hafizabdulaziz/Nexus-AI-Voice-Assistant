# Nexus Voice Assistant

Nexus is an intelligent, modular personal voice assistant built for Windows. It leverages AI, speech recognition, and system automation to help you manage your daily tasks, interact with your computer, and answer questions.

## Features

- **Voice Interaction:** Natural language processing for command execution.
- **AI Integration:** Uses Ollama (Llama 3.2) for intelligent, conversational responses.
- **Task Automation:** Open applications, websites, and folders.
- **System Monitoring:** Check battery, internet, and system stats.
- **Productivity:** File management (create, read, write, delete), note-taking, and screenshots.
- **Information Retrieval:** Get current time, date, and weather updates.

## Technologies Used

- **Python**
- **Libraries:**
  - `SpeechRecognition`: Voice-to-text conversion.
  - `pyttsx3`: Text-to-speech engine.
  - `Ollama`: Local LLM integration.
  - `OpenWeatherMap API`: Weather data.
  - `PyAutoGUI`: System automation (screenshots).
  - `psutil`: System monitoring.
  - `requests`: Network requests.
  - `JSON`: Local data persistence.

## Architecture

Nexus follows a modular architecture:
- `core.py`: Handles configuration, state, and core interaction (TTS, AI).
- `actions.py`: Contains specific tasks like weather lookup, file operations, and system automation.
- `utils.py`: Manages voice input processing.
- `main.py`: The entry point and command router.

## Project Structure

```
nexus_voice_assistant/
├── assets/             # Project assets
├── screenshots/        # Saved screenshots
├── voice_assistant/    # Source code package
│   ├── __init__.py
│   ├── main.py
│   ├── actions.py
│   ├── core.py
│   └── utils.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/hafizabdulaziz/Nexus-AI-Voice-Assistant.git
   cd Nexus-AI-Voice-Assistant
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running

```bash
python -m voice_assistant
```

## Commands Supported

| Command | Action |
| :--- | :--- |
| hello | Greets the user |
| time | Tells current time |
| date | Tells current date |
| weather [city] | Reports weather |
| search [query] | Searches Google |
| create file [name] | Creates a text file |
| screenshot | Takes a screenshot |
| battery | Reports battery status |
| goodbye | Exits the assistant |

## AI Features
Nexus integrates with [Ollama](https://ollama.ai/) to run local language models. It provides a conversational interface for general questions.

## License
MIT

## Author
Abdul Aziz
