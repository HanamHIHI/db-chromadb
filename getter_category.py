# ChromaDB 클라이언트 및 컬렉션 설정
import chromadb
import pandas as pd

client_restaurant = chromadb.PersistentClient()

collection = client_restaurant.get_collection(name="category_db")

# print(collection.peek())

results = collection.query(
        query_embeddings=[0.15] * 768,
        n_results=10,
    )

print(results)
print(len(results["ids"][0]))