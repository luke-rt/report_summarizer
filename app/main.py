import os
import PyPDF2
from PIL import Image
import pytesseract

# Directory for storing PDF resumes and job applications
pdf_directory = '/datasets/raw'

# Directory for storing extracted text from PDFs
text_directory = '/datasets/out/text'

# OCR output directory for scanned PDFs
ocr_directory = '/datasets/content/out/ocr'

# Create directories if they don't exist
os.makedirs(pdf_directory, exist_ok=True)
os.makedirs(text_directory, exist_ok=True)
os.makedirs(ocr_directory, exist_ok=True)
