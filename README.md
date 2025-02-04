# Agriventure: Agriculture ChatBot

Agriventure is a chatbot designed to provide agriculture-related information using **Streamlit** for the UI and **Google Generative AI** for responses.

## Features
- Real-time chat interface with **Streamlit**.
- AI-generated agriculture-specific responses.
- Easy setup with **python-dotenv** for environment variables.

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/agriventure-chatbot.git
   cd agriventure-chatbot
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Key:**
   - Create a `.env` file:
     ```env
     GEMINI_API_KEY=your_google_api_key_here
     ```

## Run the ChatBot
```bash
streamlit run main.py
```

## Project Structure
```
agriventure-chatbot/
├── main.py          # Streamlit UI
├── backend.py       # AI response logic
├── .env             # API key
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

## Requirements
- **streamlit**
- **google-generativeai**
- **python-dotenv**


Enjoy using **Agriventure**! 🌿

