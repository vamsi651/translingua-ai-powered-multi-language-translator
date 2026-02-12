# 🌐 AI-Powered Language Translator

## Overview

This project is a simple AI-based multilingual translator built using **Streamlit** and **Google Gemini API**. It allows users to enter text, choose a source language, select a target language, and generate translations instantly using a generative AI model.

The application focuses on a clean UI and fast translation workflow, making it suitable for beginners learning AI integration with web apps.

---

## 🚀 Features

* AI-based text translation using Gemini Flash model
* Interactive Streamlit web interface
* Multiple language selection
* Environment variable support for secure API keys
* Simple and lightweight project structure

---

## 🧱 Tech Stack

* Python
* Streamlit
* Google Generative AI (Gemini API)
* python-dotenv

---

## 📂 Project Structure

```
Project/
│── translang.py        # Main Streamlit application
│── requirements.txt    # Project dependencies
│── .env                # API key configuration (not shared publicly)
```

---

## ⚙️ Installation

### 1. Clone or Download the Project

```
git clone <your-repository-link>
cd Project
```

### 2. Create Virtual Environment (Recommended)

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file inside the project folder and add your Gemini API key:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```
streamlit run translang.py
```

After running, Streamlit will open the app in your browser.

---

## 🧪 How It Works

1. User enters text in the input box.
2. User selects source and target languages.
3. The app sends a prompt to the Gemini model.
4. The AI generates translated text and displays it on the screen.

---

## ⚠️ Notes

* Do not upload your `.env` file to GitHub.
* API usage may incur costs depending on your Gemini quota.
* The current language list is fixed in the UI. Modify `translang.py` to add more languages.

---

## 📌 Future Improvements

* Add more language options dynamically
* Speech-to-text support
* Text-to-speech output
* Translation history
* Better error handling and validation
