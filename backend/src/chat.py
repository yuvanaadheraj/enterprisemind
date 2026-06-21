from ollama import chat

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

from config import MODEL_NAME, TOP_K
from logger import logger


embedding_model = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


def get_database(db_name):

    return Chroma(
        persist_directory=f"vectorstores/{db_name}_db",
        embedding_function=embedding_model
    )


def calculate_confidence(doc_count):

    if doc_count >= 3:
        return "High"

    elif doc_count == 2:
        return "Medium"

    return "Low"


def ask_question(question):

    logger.info(f"Question: {question}")

    print("\nSearching All Databases...")

    hr_docs = get_database("hr").similarity_search(
        question,
        k=2
    )

    project_docs = get_database("project").similarity_search(
        question,
        k=2
    )

    technical_docs = get_database("technical").similarity_search(
        question,
        k=2
    )

    docs = hr_docs + project_docs + technical_docs

    sources = []

    print("\nRetrieved Documents:")

    for doc in docs:

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        sources.append(source)

        print(source)

    logger.info(f"Sources: {sources}")

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    prompt = f"""
You are EnterpriseMind.

Answer ONLY using the provided context.

If the answer is not present in the context,
reply exactly:

I could not find that information.

Context:
{context}

Question:
{question}
"""

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    confidence = calculate_confidence(
        len(docs)
    )

    answer += f"\n\nConfidence: {confidence}"

    if sources:

        answer += "\n\nSources:\n"

        for source in sorted(
            set(sources)
        ):

            answer += f"- {source}\n"

    logger.info("Answer Generated")

    return answer


if __name__ == "__main__":

    while True:

        query = input("\nAsk: ")

        if query.lower() == "exit":
            break

        answer = ask_question(query)

        print("\nAnswer:")
        print(answer)