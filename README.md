# SemSemantic Search in PDFs

This repository provides four python scripts to quickly setup a lightweight search engine for your PDFs. It uses sentence transformers to convert sentences to semantic vectors, which are then stored in a SQLite3 database. 

## Getting Started

Follow these steps to process all PDFs in a folder and setup your own semantic search engine.

1. Run pdf_embedder.py on all the PDFs of your library.
2. Empty the vecdb folder.
3. Run chroma_vector_db.py to create the SQLite3 database.
4. Run chromadb_server.py to test the search.

## Scripts

### pdf_embedder.py 

This script processes a given PDF file and converts each sentence into a semantic vector using sentence transformers model. It then stores these vectors, along with the sentence it corresponds to and some metadata such as the page number and index of the sentence on the page, in a JSON file.

### chroma_vector_db.py

This script creates an SQLite3 database and adds the sentence vectors from the JSON file created by the pdf_embedder.py script to the database.

### chromadb_server.py

This script queries the SQLite3 database created by the chroma_vector_db.py script. It converts a search query into a semantic vector using the same sentence transformer model, and then searches the database for the closest matching vectors.

## Prerequisites

You need to have Python 3.8+ installed along with the following libraries:

```
fitz
nltk
re
sentence_transformers
chromadb
```

You can install these packages using pip:

```pip install PyMuPDF nltk regex sentence-transformers chromedb```

## Note

You might need to adjust the paths in these scripts to correctly point to your own directories.