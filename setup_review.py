# ChromaDB 클라이언트 및 컬렉션 설정
import chromadb
import pandas as pd
from tqdm import tqdm

client_review = chromadb.PersistentClient()

try:
    client_review.delete_collection(name="review_db")
except:
    print("none")
    pass

collection_restaurant = client_review.create_collection(name="review_db", metadata={"hnsw:space": "cosine", "hnsw:M": 1024})

df = pd.read_csv("df_final_v7.csv")
df_review = pd.read_csv("preprocessed_urls_hanam_restaurant_real_url_review.csv")
df_vectors = pd.read_csv("hanam_vectors_100000_v2.csv",header=None)
df_category = pd.read_csv("category_embedding_v7.csv")

category_list = ['해물 요리', '한식당', '일식당', '양식', '고기 요리', '카페', '식당', '디저트',
       '햄버거', '식당 아님', '분식', '치킨', '맥주', '피자', '중국집', '베이커리', '아시안 음식',
       '야채 요리', '주류']

# print(df_vectors.iloc[0])
print(type(df_vectors.iloc[0].shape), df_vectors.iloc[0].shape)

# # 768차원 벡터 데이터
# embeddings = [[0.1] * 768, [0.2] * 768]  # 768차원 벡터
# ids = ["vec1", "vec2"]

# # 메타데이터 추가 가능
# metadatas = [
#     {"label": "vector1", "value": 100},
#     {"label": "vector2", "value": 200}
# ]

embeddings_review = []
ids_review = []
metadatas_review = []

for i in tqdm(range(len(df_review))):
    # print(df_review.iloc[i]["name"], type(df_review.iloc[i]["name"]))
    # print(i, df_review.iloc[i]["name"], df.loc[df["name"]==df_review.iloc[i]["name"]]["category3"].values[0])
    embeddings_review.append(list(df_vectors.iloc[i]))
    ids_review.append("review:"+str(i))
    metadatas_review.append({
        "index": i,
        "name": str(df_review.iloc[i]["name"]) if (pd.isna(df_review.iloc[i]["name"])==False) else '',
        "category0": str(df.loc[df["name"]==df_review.iloc[i]["name"]]["category3"].values[0]) if ((len(df.loc[df["name"]==df_review.iloc[i]["name"]]["category3"])!=0) and (pd.isna(df.loc[df["name"]==df_review.iloc[i]["name"]]["category3"].values[0])==False)) else '식당',
    })

collection_restaurant.add(
    embeddings=embeddings_review,
    ids=ids_review,
    metadatas=metadatas_review  # 선택적으로 메타데이터 포함
)

print("collection_review done.")

