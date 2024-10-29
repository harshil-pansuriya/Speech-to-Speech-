from transformers import pipeline

# Initialize the translation pipeline
translation_pipeline = pipeline("translation", model="Helsinki-NLP/opus-mt-hi-en")