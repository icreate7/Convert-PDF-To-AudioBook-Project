import os
from PyPDF2 import PdfReader
from google.cloud import texttospeech


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

pdf_text = ""
reader = PdfReader("sample.pdf")
for page in reader.pages:
    text = page.extract_text()
    if text:
        pdf_text += text

client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(text=pdf_text)


voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Standard-D",
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    speaking_rate=1,
    pitch=1
)

response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as output:
    # Write the response to the output file.
    output.write(response.audio_content)
    print('Audio content written to file "output.mp3"')