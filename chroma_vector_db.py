import chromadb
import json
client = chromadb.PersistentClient(path="/vecdb")

collection = client.create_collection(name="cn_library")
f = open("your/file/path.pdf", 'r', encoding='utf-8')
dataset = json.load(f)

collection.add(
    embeddings= dataset["embeddings"],
    documents= dataset["documents"],
    metadatas= dataset["metadatas"],
    ids= dataset["ids"]
)

print(collection)