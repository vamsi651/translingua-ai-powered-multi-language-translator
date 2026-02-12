from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Initialize Streamlit app
st.set_page_config(page_title="AI-Powered Language Translator", page_icon="🌐")
st.header("🌐 AI-Powered Language Translator")

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Initialize model (ONLY ONCE)
model = genai.GenerativeModel("models/gemini-flash-latest")

# Function to translate text
def translate_text(text, source_language, target_language):
    prompt = f"Translate the following text from {source_language} to {target_language}: {text}"
    response = model.generate_content(prompt)
    return response.text

def main():
    # User input
    text = st.text_area("📝 Enter text to translate:")

    source_language = st.selectbox(
        "🌍 Select source language:",
        ["English", "Spanish", "French", "German", "Chinese"]
    )

    target_language = st.selectbox(
        "🌍 Select target language:",
        ["English", "Spanish", "French", "German", "Chinese"]
    )

    if st.button("🔁 Translate"):
        if text and source_language and target_language:
            try:
                translated_text = translate_text(text, source_language, target_language)
                st.subheader("🗣️ Translated Text:")
                st.write(translated_text)
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")
        else:
            st.warning("⚠️ Please fill in all fields.")

# Run app
if __name__ == "__main__":
    main()