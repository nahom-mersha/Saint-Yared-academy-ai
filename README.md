# Saint Yared Academy Conversational Assistant

A real-time conversational web application that introduces users to Saint Yared Academy through a guided dialogue.

The project combines a React interface with a Flask-SocketIO backend. It uses rule-based intent detection and conversation-state management to interpret responses and determine the next dialogue step.

## Live Demo

[Open the live application](https://saint-yared-chatbot-nahom-2026-eedrg9efawbxd7ae.italynorth-01.azurewebsites.net/)

## Features

- Real-time communication with Socket.IO
- Rule-based intent detection
- State-driven conversation flow
- Soft and hard fallback handling
- Persistent chat history
- Chat reset functionality
- Chat-history export as JSON
- Responsive React interface

## Architecture

```text
React frontend
      ↓ Socket.IO
Flask-SocketIO backend
      ↓
Intent detection and conversation-state logic
      ↓
JSON-based questions, configuration, and chat history
```

## Technologies

- Python
- Flask
- Flask-SocketIO
- React
- Vite
- Socket.IO
- JSON

## Running the Project

### 1. Start the backend

```powershell
cd backend
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

The backend runs at `http://127.0.0.1:5000`.

### 2. Start the frontend

Open another terminal:

```powershell
cd frontend
npm install
npm run dev
```

Open the URL shown by Vite, normally `http://localhost:5173`.

## How It Works

The backend extracts possible intents from each user message. It checks whether an intent is valid for the current conversation state and then selects the next response.

If the input is not understood, the assistant first asks the user to rephrase it. Repeated failures activate the hard fallback and end the conversation.

## Limitations

- Intent detection is rule-based rather than machine-learning-based.
- The application is designed as a local, single-user demonstration.
- Chat history is stored in a shared JSON file.

## Author

[Nahom Mersha Alehegne](https://github.com/nahom-mersha)