import os
import subprocess
import time
import re
import uuid
from whisper_mic import WhisperMic
import ollama

ABS = r"C:\\Users\\student\\Desktop\\TTS\\piper\\"
model_path = ABS + 'en_US-hfc_male-medium.onnx'
output_dir = ABS + 'output_audio_files'
os.makedirs(output_dir, exist_ok=True)

mic = WhisperMic(model="tiny", english=True, energy=400,pause=0.5)#implementation="faster_whisper",


SYSTEM_PROMPT = "The user is speaking to you through speech to text and that text gets fed to you. So they can speak to you. Your text is converted to audio using TTS. Be concise and random and nice."

chat_history = [{'role': 'system', 'content': SYSTEM_PROMPT}]




def listen_and_transcribe():
    print("Listening...")
    result = mic.listen()
    text = result.strip()
    print(f"You said: {text}")
    return text

def get_ollama_response(chat_history):
    print("Generating response with Ollama...")
    response = ollama.chat(model='llama3.1', messages=chat_history)
    response_text = response['message']['content'].strip()
    print(f"#### Ollama response: {response_text}")
    return response_text

def speak_with_piper(text):
    text = text.replace('"', '').replace("'", "")
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    execution_folder = os.path.join(output_dir, f"audio_output_{uuid.uuid4().hex}")
    os.makedirs(execution_folder, exist_ok=True)

    for idx, sentence in enumerate(sentences):

        # sentence = sentence.replace('"', '').replace("'", "")
        output_file = os.path.join(execution_folder, f'sentence_{idx + 1}.wav')
        
        subprocess.run(f'echo "{sentence}" | piper --model {model_path} --output_file {output_file}', shell=True)
        
        os.system(f"ffplay -nodisp -autoexit {output_file}")

while True:
    
    user_text = listen_and_transcribe()

    chat_history.append({'role': 'user', 'content': user_text})
    response_text = get_ollama_response(chat_history)
    chat_history.append({'role': 'you', 'content': response_text})
    
    speak_with_piper(response_text)
    
    # time.sleep(1)
