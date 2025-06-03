# 📘 Convert PDF to Audiobook with Azure Speech

This Python project extracts text from a PDF file and converts it into an audiobook (MP3) using the [Azure Text-to-Speech API](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/text-to-speech). It's a simple tool that can help you listen to documents instead of reading them.

---

## Project Structure

````
convert-pdf-to-audiobook/
├── book.pdf              # Created from sample_text
├── PDF.py       # (Optional) If you move the FPDF code here
├── main.py               # Converts PDF → audio
├── audiobook.mp3
├── .env
├── .gitignore
└── README.md
````
## 🎯 Features

- Extracts text from PDF using `pdfplumber`
- Converts text to natural-sounding speech with Azure TTS
- Saves output as `.mp3` audio file
- Secure use of API keys via `.env`

---

## 🛠 Requirements

- Python 3.8+
- Azure Speech SDK
- PyPDF2 (optional)
- pdfplumber
- `python-dotenv`

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/convert-pdf-to-audiobook.git
cd convert-pdf-to-audiobook
```

2. Create and activate a virtual environment:
```bash 
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
```
