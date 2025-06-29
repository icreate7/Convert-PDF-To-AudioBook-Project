📖 PDF to Audiobook Converter 🎧

This Python project converts any text-based PDF file into a high-quality AI-generated audiobook using **Google Cloud Text-to-Speech (TTS)**.

AI voice technology has advanced significantly — this tool lets you turn your PDFs into lifelike audio, ideal for learning, accessibility, or simply listening to books.

---

Features

✅ Extracts text from PDF files  
✅ Uses Google Cloud's TTS for realistic speech output  
✅ Outputs audio as `.mp3` files  
✅ Customizable voice, pitch, and speed  

---

Requirements

- Python 3.7+  
- Google Cloud account with **Text-to-Speech API** enabled  
- Google Cloud **Service Account JSON credentials**  

---

Project Structure

pdf_to_audiobook/
├── main.py # Main Python script
├── requirements.txt # Project dependencies
├── .gitignore # Excludes credentials/audio files
├── sample.pdf # Example PDF (optional)
└── credentials.json # Google Cloud credentials (excluded from GitHub)

yaml
Copy
Edit

---

Setup Instructions

1️⃣ Install Dependencies
in terminal type:
  pip install -r requirements.txt
  
2️⃣ Google Cloud Credentials
Enable Text-to-Speech API in your Google Cloud account

Generate a Service Account Key (JSON file)

Place credentials.json in the project directory

3️⃣ Run the Script
bash
Copy
Edit
python main.py
By default, converts sample.pdf to output.mp3

Modify main.py to change PDF file or voice settings

🎛️ Customization
In main.py, adjust:

python
Copy
Edit
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Wavenet-D",  # Choose different voices
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    speaking_rate=1,
    pitch=1
)
Explore available Google Cloud voices here

⚠️ Security Note
credentials.json contains sensitive API keys — never upload it to GitHub.
Ensure .gitignore includes:

pgsql
Copy
Edit
credentials.json
*.mp3
