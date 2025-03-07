# ChromaDB 클라이언트 및 컬렉션 설정
import chromadb
from chromadb.config import Settings
import pandas as pd

# client_category = chromadb.Client(Settings(persist_directory="category_directory"))

client_category = chromadb.PersistentClient()

try:
    client_category.delete_collection(name="category_db")
except:
    print("none")
    pass

collection_category = client_category.create_collection(name="category_db", metadata={"hnsw:space": "cosine"})

df = pd.read_csv("df_final_v7.csv")
df_mean_vectors = pd.read_csv("hanam_mean_vectors_100000_v2.csv",header=None)
df_category = pd.read_csv("category_embedding_v7.csv")

category_list = ['해물 요리', '한식당', '일식당', '양식', '고기 요리', '카페', '식당', '디저트',
       '햄버거', '식당 아님', '분식', '치킨', '맥주', '피자', '중국집', '베이커리', '아시안 음식',
       '야채 요리', '주류']

print(df_mean_vectors.iloc[0])
print(type(df_mean_vectors.iloc[0].shape), df_mean_vectors.iloc[0].shape)

embeddings_cate = []
ids_cate = []
metadatas_cate = []

for i in range(len(df_category)):
    embeddings_cate.append(list(df_category.iloc[i]))
    ids_cate.append("category"+str(i))
    metadatas_cate.append({
        "index": i,
        "category0": category_list[i],
    })

collection_category.add(
    embeddings=embeddings_cate,
    ids=ids_cate,
    metadatas=metadatas_cate  # 선택적으로 메타데이터 포함
)

print("collection_category done.")