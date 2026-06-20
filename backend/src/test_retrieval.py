from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

embedding_model = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="vectorstores/hr_db",
    embedding_function=embedding_model
)

query = "How many casual leaves are allowed?"

results = db.similarity_search(query, k=3)

print("\nRESULTS\n")

for doc in results:
    print(doc.page_content)
    print("-" * 50)