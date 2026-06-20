from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings


embedding_model = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


def load_txt_documents(folder_path):
    docs = []

    for file in Path(folder_path).glob("*.txt"):
        content = file.read_text(encoding="utf-8")

        docs.append(
            Document(
                page_content=content,
                metadata={"source": str(file)}
            )
        )

    return docs


def build_vector_db(data_folder, persist_dir):

    documents = load_txt_documents(data_folder)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_dir
    )

    print(f"Created DB: {persist_dir}")
    print(f"Chunks: {len(chunks)}")


if __name__ == "__main__":

    build_vector_db(
        "data/hr",
        "vectorstores/hr_db"
    )

    build_vector_db(
        "data/projects",
        "vectorstores/project_db"
    )

    build_vector_db(
        "data/technical",
        "vectorstores/technical_db"
    )

    print("All databases created successfully.")