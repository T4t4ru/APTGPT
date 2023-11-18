import fitz  # PyMuPDF
import os
import nltk
import pandas as pd
import re

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def preprocess_text(text):
    text = re.sub(r'\W+', ' ', text)
    sentences = sent_tokenize(text)
    return sentences

def process_pdf(file_path):
    document = fitz.open(file_path)
    text = ""
    for page in document:
        text += page.get_text()
    document.close()
    return text

def process_pdfs_in_directory(directory):
    all_sentences = []
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            filepath = os.path.join(directory, filename)
            pdf_text = process_pdf(filepath)
            processed_text = preprocess_text(pdf_text)
            all_sentences.extend(processed_text)
    return all_sentences
  
directory = '/home/luna/2023/'
processed_sentences = process_pdfs_in_directory(directory)
df = pd.DataFrame({'sentence': processed_sentences})
df.to_csv('processed_pdfs_2023.csv', index=False)
