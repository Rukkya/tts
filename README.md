# Advanced Multi-Language Text-to-Speech (TTS)

## 📌 Overview
This project is a **Text-to-Speech (TTS) application** built using **gTTS (Google Text-to-Speech) and Gradio**. It allows users to convert text into speech in multiple languages and supports bulk processing of text files such as **TXT, PDF, and DOCX**.

## 🚀 Features
- **Multi-Language Support**: Convert text to speech in different languages including **English, French, Spanish, German, Italian, and Arabic**.
- **Bulk File Processing**: Supports **TXT, PDF, and DOCX** files for converting large text content into speech.
- **Multiple Speech Speeds**: Choose between **Normal** and **Slow** speech speeds.
- **Multiple Audio Formats**: Supports **MP3** and **WAV** formats for output.
- **Gradio Web Interface**: Provides an interactive UI to enter text or upload files.
- **Text Limit Handling**: Supports up to **5000 characters** for bulk files and **500 characters** for direct text input.

## 🎤 How It Works
1. **Enter text manually** or **upload a document**.
2. **Choose language**, speech speed, and audio format.
3. Click **Generate Speech**.
4. **Listen** to the generated speech or **download** the file.

## 🏗️ gTTS Architecture
Google Text-to-Speech (gTTS) converts text into speech using Google's API. The process involves:
1. **Text Processing**: The input text is tokenized and converted into phonemes.
2. **Speech Synthesis**: Google’s deep learning models generate a natural-sounding waveform.
3. **Audio Output**: The final output is stored as an MP3 or WAV file.

## 📜 Requirements
- Python 3.7+
- gTTS
- Gradio
- PyPDF2 (for PDF file processing)
- python-docx (for DOCX file processing)
- pydub (for audio conversion)

## 🔧 Installation
```bash
pip install gtts gradio PyPDF2 python-docx pydub
```

## 📌 Usage
Run the application:
```bash
python app.py
```

This will launch a **web-based UI** where you can enter text or upload files for speech synthesis.

## 🖥️ Project Structure
```
/tts_project
│── app.py             # Main Python script
│── requirements.txt   # Required dependencies
│── README.md          # Documentation
│── example_files/     # Sample input files (TXT, PDF, DOCX)
```

## 🌍 Supported Languages
- English (US, UK)
- French
- Spanish
- German
- Italian
- Arabic

## 🛠️ Future Enhancements
- **Emotion-based TTS** (Happy, Sad, Angry, Excited)
- **SSML (Speech Synthesis Markup Language) Support**
- **Voice Cloning & Neural TTS Integration**

---
✅ **Enjoy high-quality TTS conversion with gTTS and Gradio!** 🚀

