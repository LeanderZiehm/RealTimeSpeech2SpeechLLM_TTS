# 🎙️ Real-Time Speech-to-Text & Text-to-Speech Chatbot 

A Python-based chatbot that listens to speech, transcribes it to text, generates responses using Ollama's model, and converts text replies back into spoken audio using Piper.

## ✨ Features
- 🎤 **Speech-to-Text:** Uses `WhisperMic` to capture and transcribe speech input.
- 💬 **Conversational AI:** Interacts with Ollama's `llama3.1` model for intelligent responses.
- 🔈 **Text-to-Speech:** Converts replies to speech with the Piper TTS system.
- 🔄 **Real-Time Processing:** Listens and responds in real-time.

## 📁 Setup
1. **Install Dependencies:**  
   - `pip install -r requirements.txt`
2. **Place Files:** Ensure the `tools`, `piper`, and `output_audio_files` folders are in the project directory.
3. **Configure Paths:** Edit paths for `ffplay`, `piper.exe`, and `model_path` in the script if needed.

## 🚀 Usage
1. Run the script:
   ```bash
   python chatbot.py
   ```
2. Speak to the chatbot, and it will respond with generated audio.

## 📦 File Structure
- `tools/`: Contains `ffplay` and `piper` executables.
- `output_audio_files/`: Stores audio files generated during interaction.

## 📌 Notes
- Customize the `SYSTEM_PROMPT` to change the chatbot's personality.
- **OS Compatibility:** This code is designed for Windows.

**Enjoy seamless, spoken conversations with your chatbot!**



USING:
Piper
https://github.com/rhasspy/piper

Whisper Mic
https://github.com/rhasspy/piper

ffplay 
https://www.ffmpeg.org/download.html