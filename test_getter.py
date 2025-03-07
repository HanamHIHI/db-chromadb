# ChromaDB 클라이언트 및 컬렉션 설정
import chromadb
from chromadb.config import Settings
import pandas as pd

client_restaurant = chromadb.PersistentClient()

collection = client_restaurant.get_collection(name="review_db")

# print(collection.peek())

results = collection.query(
        query_embeddings=[0.15] * 768,
        where={"$and": [{"category0": {"$ne": "식당 아님"}}, {"category0": {"$ne": ''}}]},
        n_results=10,
    )

print(results)
print(len(results["ids"][0]))