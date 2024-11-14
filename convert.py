# from Mistral Large 2 model
# Nov 14, 2024

import os
import chardet
import subprocess

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def convert_to_ansi(file_path):
    output_file_path = file_path.replace('.lrc', '_ansi.lrc')
    subprocess.run(['iconv', '-f', 'UTF-8', '-t', 'CP936', file_path, '-o', output_file_path])
    print(f"Converted {file_path} to {output_file_path}")

def main():
    # 假设你的歌词文件在当前目录下
    for file_name in os.listdir('.'):
        if file_name.endswith('.lrc'):
            file_path = os.path.join('.', file_name)
            encoding = detect_encoding(file_path)
            print(f"File: {file_name}, Encoding: {encoding}")
            if encoding != 'CP936':
                convert_to_ansi(file_path)