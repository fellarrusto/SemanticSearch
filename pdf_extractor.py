import json
import re
import fitz  # PyMuPDF
from PyPDF2 import PdfFileReader
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')

def extract_information(pdf_path):
    sentences = {}
    doc = fitz.open(pdf_path)
    book_id = 1  # replace with actual logic to get book id
    sentence_number = 1
    for page in range(len(doc)):
        text = doc.load_page(page).get_text("text")
        # detect the newline characters "-"
        text = re.sub('-\n', '', text)
        text = re.sub('-', '', text)
        text = re.sub('\n', ' ', text)
        # split text into sentences
        sents = sent_tokenize(text)
        for sent in sents:
            # construct the code
            code = f"B{book_id}P{page}S{sentence_number}"
            sentences[code] = {
                'book_id': book_id,
                'page_number': page,
                'sentence_number': sentence_number,
                'sentence': sent
            }
            sentence_number += 1
    return sentences

def save_to_json(sentences, json_path):
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(sentences, f, ensure_ascii=False, indent=4)

pdf_dir = "F:/CorsariNeri/Biblioteca/Libri/OCR/"
pdf_name = "(S.Agnello) Le Strade di S.Agnello - Franco Gargiulo.pdf"
pdf_path = pdf_dir + pdf_name
json_path = f'{pdf_name}result.json'

sentences = extract_information(pdf_path)
save_to_json(sentences, json_path)