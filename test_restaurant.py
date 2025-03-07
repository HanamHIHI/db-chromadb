# ChromaDB 클라이언트 및 컬렉션 설정
import chromadb
from chromadb.config import Settings
import pandas as pd

client_restaurant = chromadb.PersistentClient()

try:
    client_restaurant.delete_collection(name="restaurant_db")
except:
    print("none")
    pass

collection_restaurant = client_restaurant.create_collection(name="restaurant_db", metadata={"hnsw:space": "cosine"})

df = pd.read_csv("df_final_v7.csv")
df_mean_vectors = pd.read_csv("hanam_mean_vectors_100000_v2.csv",header=None)
df_category = pd.read_csv("category_embedding_v7.csv")

category_list = ['해물 요리', '한식당', '일식당', '양식', '고기 요리', '카페', '식당', '디저트',
       '햄버거', '식당 아님', '분식', '치킨', '맥주', '피자', '중국집', '베이커리', '아시안 음식',
       '야채 요리', '주류']

print(df_mean_vectors.iloc[0])
print(type(df_mean_vectors.iloc[0].shape), df_mean_vectors.iloc[0].shape)

# # 768차원 벡터 데이터
# embeddings = [[0.1] * 768, [0.2] * 768]  # 768차원 벡터
# ids = ["vec1", "vec2"]

# # 메타데이터 추가 가능
# metadatas = [
#     {"label": "vector1", "value": 100},
#     {"label": "vector2", "value": 200}
# ]

embeddings_rest = []
ids_rest = []
metadatas_rest = []

for i in range(len(df)):
    embeddings_rest.append(list(df_mean_vectors.iloc[i]))
    ids_rest.append("restaurant"+str(i))
    metadatas_rest.append({
        "index": int(df.iloc[i]["index"]),
        "name": str(df.iloc[i]["name"]) if (pd.isna(df.iloc[i]["name"])==False) else '',
        "addr": str(df.iloc[i]["position"]) if (pd.isna(df.iloc[i]["name"])==False) else '',
        "dist": int(df.iloc[i]["total_distance"]) if (pd.isna(df.iloc[i]["name"])==False) else -1,
        "reqtime": int(df.iloc[i]["total_time"]) if (pd.isna(df.iloc[i]["name"])==False) else -1,
        "category0": str(df.iloc[i]["category3"]) if (pd.isna(df.iloc[i]["name"])==False) else '',
    })

collection_restaurant.add(
    embeddings=embeddings_rest,
    ids=ids_rest,
    metadatas=metadatas_rest  # 선택적으로 메타데이터 포함
)

print("collection_restaurant done.")

