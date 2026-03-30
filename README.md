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

## Example Use Cases

- Document question answering systems for businesses  
- Internal knowledge assistants for company documents  
- Research paper summarization and analysis  
- Policy and compliance document search  
- AI-powered workflow automation for document-heavy processes  

## Future Improvements

- Support for multiple documents and knowledge bases  
- Citation-based answers with source referencing  
- Conversational memory across multiple queries  
- OCR integration for scanned and image-based PDFs  
- Deployment on cloud platforms (Streamlit Cloud, AWS, Docker)  

## Installation

```bash
git clone <your-repository-url>
cd ai-document-chatbot
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt