import os
import subprocess
import time
import re
import uuid

input_file = 'input.txt'
model_path = 'en_US-hfc_male-medium.onnx'
output_dir = 'output_audio_files'

execution_folder = os.path.join(output_dir, f"audio_output_{uuid.uuid4().hex}")
os.makedirs(execution_folder, exist_ok=True)

with open(input_file, 'r') as f:
    text = f.read()

sentences = re.split(r'(?<=[.!?])\s+', text.strip())

for idx, sentence in enumerate(sentences):
    output_file = os.path.join(execution_folder, f'sentence_{idx + 1}.wav')
    
    subprocess.run(f"echo \"{sentence}\" | piper --model {model_path} --output_file {output_file}", shell=True)
    
    os.system(f"ffplay -nodisp -autoexit {output_file}")
    
    # time.sleep(0.5)
