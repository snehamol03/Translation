import streamlit as st
from transformers import pipeline

def main():
    st.title("Language Translator")

    # Define language options
    languages = {
        "English": "en",
        "French": "fr",
        "German": "de",
        "Spanish": "es",
        "Hindi": "hi",
        "Tamil": "ta"
    }

    # Select source and target languages
    source_language = st.selectbox("Select Source Language:", list(languages.keys()))
    target_language = st.selectbox("Select Target Language:", list(languages.keys()))

    # Input text
    input_text = st.text_area("Enter text to translate:")

    if st.button("Translate"):
        if source_language == target_language:
            st.write("Source and target languages cannot be the same.")
        else:
            model_name = f"Helsinki-NLP/opus-mt-{languages[source_language]}-{languages[target_language]}"
            try:
                # Load the translation pipeline
                translator = pipeline("translation", model=model_name)
                # Perform translation
                translated = translator(input_text, max_length=400)
                translated_text = translated[0]['translation_text']
                st.write(f"Translated text from {source_language} to {target_language}:")
                st.write(translated_text)
            except Exception as e:
                st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
