import os
import subprocess
import re
import uuid
import time
import pyperclip
import keyboard

input_file = 'input.txt'
# model_path = 'en_US-hfc_male-medium.onnx'
#model_path = 'en_GB-semaine-medium.onnx'
model_path = 'en_US-joe-medium.onnx'





output_dir = 'output_audio_files'

execution_folder = os.path.join(output_dir, f"audio_output_{uuid.uuid4().hex}")
os.makedirs(execution_folder, exist_ok=True)

def process_and_speak():
    time.sleep(0.01)
    text = pyperclip.paste()  

    text = text.replace('"', '').replace("'", "")

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())  

    for idx, sentence in enumerate(sentences):
        output_file = os.path.join(execution_folder, f'sentence_{idx + 1}.wav')

        subprocess.run(f"echo \"{sentence}\" | piper --model {model_path} --output_file {output_file}", shell=True)

        os.system(f"ffplay -nodisp -autoexit {output_file}")  

        # time.sleep(0.5)

def pause():
    print("Processing paused.")  
    
keyboard.add_hotkey("ctrl+c", process_and_speak)  
keyboard.add_hotkey("ctrl+q", pause)  

print("Press Ctrl+C to start speaking the clipboard text or Ctrl+Q to pause.")
keyboard.wait()  
