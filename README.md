# AI-Powered Document Chatbot

An AI-powered document question-answering application built with Streamlit, OpenAI, LangChain, and FAISS.

Users can upload a PDF document and ask natural-language questions about its content. The application processes the document, creates embeddings for text chunks, retrieves the most relevant sections, and generates grounded answers using an LLM.

## Features

- Upload PDF documents
- Extract and process document text
- Split text into semantic chunks
- Generate embeddings using OpenAI
- Store and search document chunks using FAISS
- Ask natural-language questions about the document
- View retrieved context used for answering
- Maintain chat history during the session

## Tech Stack

- Python
- Streamlit
- OpenAI API
- LangChain
- FAISS
- PyPDF
- Python-dotenv

## How It Works

1. The user uploads a PDF document.
2. The app extracts text from each page.
3. The extracted text is split into smaller overlapping chunks.
4. Each chunk is converted into embeddings.
5. The embeddings are stored in a FAISS vector store.
6. When the user asks a question, the app retrieves the most relevant chunks.
7. The retrieved context is sent to the LLM to generate a grounded answer.

## Installation

```bash
git clone <your-repository-url>
cd ai-document-chatbot
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt