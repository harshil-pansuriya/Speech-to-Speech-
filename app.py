import streamlit as st
from components.audio_processing import record_audio, speech_to_hindi_text
from components.translation_tts import translate_to_english, text_to_speech

st.title("Hindi Speech to English Text-to-Speech Converter")

if st.button("Record Audio"):
    audio_data = record_audio()
    hindi_text = speech_to_hindi_text(audio_data)

    if hindi_text:
        st.write("Hindi Text:", hindi_text)

        english_text = translate_to_english(hindi_text)
        st.write("English Translation:", english_text)

        output_audio = text_to_speech(english_text)
        st.audio(output_audio)
