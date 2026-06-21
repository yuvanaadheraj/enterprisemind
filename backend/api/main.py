from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import sys
import os

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "src"
    )
)

from chat import ask_question
from document_ingestor import ingest_document


app = FastAPI(
    title="EnterpriseMind API",
    version="1.1"
)
app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


class QueryRequest(BaseModel):

    question: str


@app.get("/")
def home():

    return {
        "message":
        "EnterpriseMind Running"
    }


@app.post("/chat")
def chat_endpoint(
    request: QueryRequest
):

    answer = ask_question(
        request.question
    )

    return {
        "question":
        request.question,

        "answer":
        answer
    }


@app.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    upload_dir = "uploads"

    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    file_path = os.path.join(
        upload_dir,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as f:

        content = await file.read()

        f.write(content)

    result = ingest_document(
        file_path,
        "technical"
    )

    return {
        "filename":
        file.filename,

        "result":
        result
    }