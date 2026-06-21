from pathlib import Path

from pypdf import PdfReader

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings


embedding_model = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


def read_file(file_path):

    file_path = Path(file_path)

    if file_path.suffix == ".txt":

        return file_path.read_text(
            encoding="utf-8"
        )

    elif file_path.suffix == ".pdf":

        pdf = PdfReader(file_path)

        text = ""

        for page in pdf.pages:
            text += page.extract_text() + "\n"

        return text

    else:
        raise Exception("Unsupported file type")


def ingest_document(
    file_path,
    db_name="technical"
):

    content = read_file(file_path)

    document = Document(
        page_content=content,
        metadata={
            "source": str(file_path)
        }
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(
        [document]
    )

    db = Chroma(
        persist_directory=f"vectorstores/{db_name}_db",
        embedding_function=embedding_model
    )

    db.add_documents(chunks)

    try:
        db.persist()
    except:
        pass

    return {
        "status": "success",
        "chunks_added": len(chunks)
    }