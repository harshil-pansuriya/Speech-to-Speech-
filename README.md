# Hindi Speech to English Text-to-Speech Converter

This project is a **Hindi Speech to English Text and Speech Conversion** tool. It records Hindi audio input, transcribes it to Hindi text, translates it into English, and finally converts the translated text to English speech. This project uses **Hugging Face transformers** for the translation process and **Google Text-to-Speech (gTTS)** for speech synthesis.

## Project Overview

The application provides an easy-to-use interface to:

1. Record Hindi speech.
2. Transcribe Hindi speech to text.
3. Translate Hindi text to English.
4. Convert English text to synthesized English audio output.

## Components

### 1. `app.py`

- This is the main application file, which uses **Streamlit** to create a user interface.
- Users can record their audio, view the Hindi transcription, English translation, and play the audio of the English translation.

### 2. `audio_processing.py`

- Contains functions to record audio and convert it into Hindi text.
- Uses `speech_recognition` to capture the audio from the microphone and `asr_pipeline` for Hindi transcription.

### 3. `translation_tts.py`

- Contains functions to translate Hindi text to English and convert English text to speech.
- Uses Hugging Face's `translation` pipeline with the **Helsinki-NLP/opus-mt-hi-en** model for translating Hindi to English.
- Uses `gTTS` to synthesize English text into audio.

### 4. `file_manage.py`

- Provides utility functions to manage temporary files, such as creating and deleting temporary audio files.

## Setup Instructions

1. **Clone the Repository**:

   ```bash
    git clone https://github.com/harshil-pansuriya/Speech-to-Speech-.git
    cd yourproject_path
   ```

2. **Create a Virtual Environment:**

   ```
   python -m venv env_name
   env_name\Scripts\activate
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

## Usage Insrtuctions:

1. **Run the application:**
   ```
   streamlit run app.py
   ```

## Dependencies

- streamlit: For the user interface.
- transformers: For translation using a pretrained model.
- speechrecognition: For capturing audio input.
- gTTS: For converting text to speech.

## Model Details

- ASR (Automatic Speech Recognition): Uses asr_pipeline to transcribe Hindi speech.
- Translation: Helsinki-NLP/opus-mt-hi-en model translates Hindi text to English.
- Text-to-Speech: gTTS converts English text to speech.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
