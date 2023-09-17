import chromadb
from sentence_transformers import SentenceTransformer

# model = SentenceTransformer('./d-b-mult-cased')
model = SentenceTransformer('distiluse-base-multilingual-cased-v2')

# To save the model locally execute the following instruction
#
# model.save(modelPath)
#
# Then to use the model just call the object as follows
#
# model = SentenceTransformer(modelPath)

def compute_embedding(text, model):
  return model.encode(text)

client = chromadb.PersistentClient(path="D:/CorsariNeri/RnD/MachineLearning/SemanticSearch/vecdb")

collection = client.get_collection(name="cn_library")
embedding = compute_embedding("La vecchia abside è stata incorporata in questo imponente doppio cilindro, decorato con cornicioni in terracotta.", model)
results = collection.query(
    query_embeddings=[embedding.tolist()],
    n_results=3
)
print(results["metadatas"][0][0]["book_name"])
print(results["distances"])
print(results["metadatas"][0][0]["page_number"]+1)
print(results["metadatas"][0][1]["page_number"]+1)
print(results["metadatas"][0][2]["page_number"]+1)