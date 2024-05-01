import os
import ollama
from ollama import generate
import glob
import pandas as pd
from PIL import Image
from io import BytesIO


def get_img_files(folder_path):
    return glob.glob(f"{folder_path}/*.jpg")

image_files = get_img_files("/Text-to-audio/test-images")

def process_image(image_file):
    with Image.open(image_file) as img:
        with BytesIO() as buffer:
            img.save(buffer, format='PNG')
            image_bytes = buffer.getvalue()

    full_response = ''
    for response in generate(model='llava:7b',
                             prompt='Extract the text from the following image and give a clear description of it',
                             images=[image_bytes],
                             stream=True):
        print(response['response'], end='', flush=True)
        full_response += response['response']
    return full_response
