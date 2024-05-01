from text_to_audio import generate_audio
from Img_description import process_image, get_img_files

def main():
    image_files = get_img_files("/Users/rayaneghilene/Documents/Ollama/Text-to-audio/test-images")

    for image_file in image_files[:1]:
        text = process_image(image_file)
        generate_audio(text,  "speech.wav")

if __name__ == "__main__":
    main()