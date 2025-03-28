import gradio as gr
from gtts import gTTS
import time
import os
import docx
import PyPDF2

# Available languages with accents
LANGUAGES = {
    "English (US)": "en",
    "English (UK)": "en-uk",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Arabic (Standard)": "ar",
}

def extract_text_from_file(file):
    """Extracts text from uploaded files (PDF, TXT, DOCX)."""
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    elif file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in pdf_reader.pages])
    return None

def generate_speech(text, language, speed, audio_format):
    """Generate speech from text using gTTS."""
    if not text.strip():
        return "Error: No text provided.", None

    if len(text) > 5000:  # Increased limit for bulk files
        return "Error: Text exceeds 5000 characters.", None

    timestamp = str(int(time.time()))
    output_path = f"tts_{timestamp}.{audio_format.lower()}"

    # gTTS Processing
    tts = gTTS(text=text, lang=LANGUAGES[language], slow=(speed == "Slow"))
    tts.save(output_path)

    return output_path, output_path  # Returns file for playback & download

def process_uploaded_file(file, language, speed, audio_format):
    """Extracts text from the uploaded file and converts it to speech."""
    text = extract_text_from_file(file)
    if not text:
        return "Error: Unable to read file.", None
    return generate_speech(text, language, speed, audio_format)

# Gradio Interface
iface = gr.Interface(
    fn=generate_speech,
    inputs=[
        gr.Textbox(label="Enter text (Max 5000 characters)", lines=10),
        gr.Dropdown(list(LANGUAGES.keys()), label="Select Language", value="English (US)"),
        gr.Radio(["Normal", "Slow"], label="Speech Speed", value="Normal"),
        gr.Radio(["MP3", "WAV"], label="Audio Format", value="MP3"),
    ],
    outputs=[gr.Audio(label="Generated Speech"), gr.File(label="Download Audio")],
    title="Advanced Multi-Language Text-to-Speech",
    description="Convert text into speech with multiple languages and formats.",
)

# Bulk File Processing Interface
file_iface = gr.Interface(
    fn=process_uploaded_file,
    inputs=[
        gr.File(label="Upload File (PDF, TXT, DOCX)"),
        gr.Dropdown(list(LANGUAGES.keys()), label="Select Language", value="English (US)"),
        gr.Radio(["Normal", "Slow"], label="Speech Speed", value="Normal"),
        gr.Radio(["MP3", "WAV"], label="Audio Format", value="MP3"),
    ],
    outputs=[gr.Audio(label="Generated Speech"), gr.File(label="Download Audio")],
    title="Bulk File Text-to-Speech",
    description="Upload a file (PDF, TXT, DOCX) to convert its content to speech.",
)

# Combine both interfaces in a tabbed UI
gr.TabbedInterface(
    [iface, file_iface],
    ["Text Input", "File Upload"]
).launch()
