from transformers import pipeline
from gtts import gTTS
from utils.file_manage import create_temp_file

# Initialize pipelines
translation_pipeline = pipeline("translation", model="Helsinki-NLP/opus-mt-hi-en")

def translate_to_english(hindi_text):
    return translation_pipeline(hindi_text)[0]['translation_text']

def text_to_speech(english_text):
    tts = gTTS(text=english_text, lang='en')
    temp_file_path = create_temp_file(tts.save, suffix=".mp3")
    return temp_file_path
