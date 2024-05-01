from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan, set_seed
from datasets import load_dataset
import soundfile as sf
import torch
import argparse

def main():
    parser = argparse.ArgumentParser(description="Text-to-Speech with Speaker Embeddings")
    parser.add_argument("input_file", help="Path to the input text file")
    args = parser.parse_args()
    embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")

    speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

    processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
    model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
    vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

    with open(args.input_file, "r", encoding="utf-8") as file:
        input_text = file.read()

    inputs = processor(text=input_text, return_tensors="pt")

    set_seed(555)
    speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)
    sf.write("speech.wav", speech.numpy(), samplerate=16000)

if __name__ == "__main__":
    main() 
