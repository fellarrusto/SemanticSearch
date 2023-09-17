import json
import fitz  # PyMuPDF
import nltk
import re
from sentence_transformers import SentenceTransformer

nltk.download("punkt")
from nltk.tokenize import sent_tokenize

def compute_embedding(text, model):
  return model.encode(text)

def extract_information(pdf_path, title, model, start_id):
    embeddings = []
    documents = []
    metadatas = []
    ids = []
    id = start_id
    doc = fitz.open(pdf_path)
    book_id = 1  # replace with actual logic to get book id
    print("Start processing")
    for page in range(len(doc)):
        print(f"Computing page {page}")
        text = doc.load_page(page).get_text("text")
        text = re.sub(r'\s+', " ", text)
        text = re.sub(r"[\'\"`]", "", text)
        sentences = sent_tokenize(text)  # Suddivide il testo in frasi

        for sentence in sentences:
            embeddings.append(compute_embedding(sentence, model).tolist())
            documents.append(sentence)
            meta = {
                "book_id": book_id,
                "book_name": title,
                "page_number": page,
                "sentence_index": sentences.index(sentence),
            }
            metadatas.append(meta)
            ids.append(str(id))
            id+=1
    return {"embeddings": embeddings, "documents": documents, "metadatas": metadatas, "ids": ids}

def save_to_json(sentences, json_path):
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(sentences, f, ensure_ascii=False, indent=4)

# model = SentenceTransformer('./d-b-mult-cased')
model = SentenceTransformer('distiluse-base-multilingual-cased-v2')

# To save the model locally execute the following instruction
#
# model.save(modelPath)
#
# Then to use the model just call the object as follows
#
# model = SentenceTransformer(modelPath)

pdf_dir = "your/folder/"
pdf_name = "youtfile.pdf"
pdf_path = pdf_dir + pdf_name
json_path = f'{pdf_name}result.json'

sentences = extract_information(pdf_path, pdf_name, model, 0)
save_to_json(sentences, json_path)