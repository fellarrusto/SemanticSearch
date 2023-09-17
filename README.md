# PDF Semantic Search 

This repository provides four python scripts to quickly setup a lightweight search engine for your PDFs. It uses sentence transformers to convert sentences to semantic vectors, which are then stored in a SQLite3 database to perform embedding search with the vector database Chroma.

# Technologies used

**SentenceTransformer:** This library is used to generate sentence embeddings. It is specifically used with its 'distiluse-base-multilingual-cased-v2' model, which is a multilingual model.

**chromadb:** This library is used to create a database of the vectorized sentences, with data persistent on disk.

# Getting Started Instructions

1. Install all the necessary dependencies using pip:

```bash
pip install PyMuPDF nltk regex sentence-transformers chromedb
```

2. Make sure you have downloaded the nltk's 'punkt' package. You can do so using the python shell, as follows:

```python
import nltk
nltk.download('punkt')
```

3. Run the `pdf_embedder.py` script replacing the PDF file you want to process inside the code. This creates a JSON file with vector embeddings of the text in the PDF.


4. Empty the vecdb folder, if it exists from previous runs.

5. Create the SQLite3 database using `chroma_vector_db.py`, this script takes the previously generated JSON file and creates an SQLite database. 

```bash
python chroma_vector_db.py
```

6. To test the correctness of the vector embeddings and the search functionality, run the `chromadb_server.py` script. You should see printed the book name, distances and page numbers as output.

```bash
python chromadb_server.py
```

Please note that this project file paths are hard-coded and should be updated according to the location of your files and folders.
