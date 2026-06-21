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

    selected_db = route_query(question)

    print(f"\nUsing database: {selected_db}")

    db = get_database(selected_db)

    docs = db.similarity_search(
        question,
        k=3
    )

    print("\nRetrieved Documents:")

    sources = []

    for doc in docs:
        source = doc.metadata.get("source", "Unknown")
        sources.append(source)
        print(source)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are EnterpriseMind.

Answer ONLY using the provided context.

If the answer is not present in the context,
say exactly:

I could not find that information.

Context:
{context}

Question:
{question}
"""

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    if sources:
        answer += "\n\nSources:\n"

        for source in sorted(set(sources)):
            answer += f"- {source}\n"

    return answer


# Chat Loop
if __name__ == "__main__":

    while True:

        query = input("\nAsk: ")

        if query.lower() == "exit":
            break

        answer = ask_question(query)

        print("\nAnswer:")
        print(answer)