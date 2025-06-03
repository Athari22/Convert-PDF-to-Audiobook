import os
import pdfplumber
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv



# Load API credentials securely
load_dotenv()
speech_key = os.getenv("AZURE_SPEECH_KEY")
speech_region = os.getenv("AZURE_SERVICE_REGION")
# print("🔑 SPEECH KEY:", speech_key)
# print("🌍 REGION:", speech_region)


# Extract text from PDF using pdfplumber
def extract_text_with_plumber(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"❌ Failed to read PDF: {e}")
    return text

# Convert text to speech using Azure
def text_to_speech(text, output_file):
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file)
    speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"  # Change to another voice if needed
    
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    
    # Azure TTS can fail on very long input; so consider chunking if needed
    if len(text) > 5000:
        print("Splitting text due to Azure size limits...")
        text_chunks = [text[i:i + 4000] for i in range(0, len(text), 4000)]
        with open(output_file, 'wb') as f:
            for chunk in text_chunks:
                result = synthesizer.speak_text_async(chunk).get()
                if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                    f.write(result.audio_data)
                else:
                    print("Speech synthesis failed:", result.reason)
    else:
        result = synthesizer.speak_text_async(text).get()
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"✅ Audio saved to {output_file}")
        else:
            print("❌ Speech synthesis failed:", result.reason)


# Main usage
if __name__ == "__main__":
    pdf_path = "book.pdf"
    output_audio = "audiobook.mp3"
    
    if not os.path.exists(pdf_path):
        print(f"❌ File '{pdf_path}' not found.")
    else:
        print("📖 Extracting text...")
        pdf_text = extract_text_with_plumber(pdf_path)
        
        if pdf_text.strip() == "":
            print("❌ No text extracted from the PDF.")
        else:
            print("🔊 Converting text to speech...")
            text_to_speech(pdf_text, output_audio)
