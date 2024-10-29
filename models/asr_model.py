from transformers import pipeline

# Initialize the ASR pipeline
asr_pipeline = pipeline("automatic-speech-recognition", model="theainerd/Wav2Vec2-large-xlsr-hindi")