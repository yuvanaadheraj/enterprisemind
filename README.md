# EnterpriseMind

EnterpriseMind is an AI-powered enterprise knowledge assistant that enables employees to query company documents using natural language.

The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from company knowledge bases and uploaded documents before generating answers using a Large Language Model (LLM).

---

## Features

* Enterprise document Q&A
* Multi-database retrieval
* FastAPI backend
* React frontend
* ChromaDB vector database
* Ollama + Qwen3 integration
* Document upload support
* Automatic document ingestion
* Source attribution
* Confidence scoring

---

## Architecture

```text
React Frontend
       |
       v
FastAPI Backend
       |
       v
ChromaDB Vector Store
       |
       v
Ollama (Qwen3)
```

---

## Project Structure

```text
EnterpriseMind/

├── backend/
│   ├── api/
│   ├── src/
│   ├── uploads/
│   ├── data/
│   ├── vectorstores/
│   ├── config.py
│   ├── logger.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## Technologies Used

### Backend

* FastAPI
* LangChain
* ChromaDB
* Ollama
* Qwen3
* Sentence Transformers

### Frontend

* React
* Vite
* Axios
* Tailwind CSS

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yuvanaadheraj/enterprisemind.git
cd enterprisemind
```

### Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

## Run Backend

```bash
cd backend

python -m uvicorn api.main:app --reload
```

---

## API Endpoints

### Chat

```http
POST /chat
```

Request:

```json
{
  "question": "What is FastAPI?"
}
```

### Upload

```http
POST /upload
```

Upload TXT or PDF documents.

---

## Example Questions

* What is FastAPI?
* What modules are present in EnterpriseMind?
* How many annual leaves do employees receive?
* What information is contained in the uploaded document?

---

## Future Improvements

* Similarity score ranking
* Role-based access control
* User authentication
* Cloud deployment
* Dashboard analytics
* Multi-user support

---

## Author

Yuvan Aadheraj

B.Tech CSE

EnterpriseMind - Enterprise Knowledge Assistant
