from ollama import chat

from router_agent import route_query
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings


# Embedding Model
embedding_model = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


# Load Correct Database
def get_database(db_name):

    return Chroma(
        persist_directory=f"vectorstores/{db_name}_db",
        embedding_function=embedding_model
    )


# Main Function
def ask_question(question):

    # Select database using router agent
    selected_db = route_query(question)

    print(f"\nUsing database: {selected_db}")

    db = get_database(selected_db)

    # Retrieve relevant chunks
    docs = db.similarity_search(
        question,
        k=3
    )

    print("\nRetrieved Documents:")

    for doc in docs:
        print(doc.metadata)

    # Build context
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Prompt
    prompt = f"""
You are EnterpriseMind.

Answer ONLY using the provided context.

If the answer is not present in the context,
say:

'I could not find that information.'

Context:
{context}

Question:
{question}
"""

    # Ask Ollama
    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


# Chat Loop
while True:

    query = input("\nAsk: ")

    if query.lower() == "exit":
        break

    answer = ask_question(query)

    print("\nAnswer:")
    print(answer)