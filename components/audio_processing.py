import streamlit as st
import speech_recognition as sr
from utils.file_manage import create_temp_file, delete_temp_file
from models.asr_model import asr_pipeline

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Recording... Please speak now.")
        audio_data = recognizer.listen(source)
        st.success("Recording complete.")
    return audio_data

def speech_to_hindi_text(audio_data):
    temp_file_path = create_temp_file(audio_data.get_wav_data(), suffix=".wav")

    try:
        result = asr_pipeline(temp_file_path)
        return result['text']
    except Exception as e:
        st.error(f"Error in speech recognition: {e}")
        return None
    finally:
        delete_temp_file(temp_file_path)
