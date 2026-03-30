import os

import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Document Chatbot", page_icon="📄", layout="wide")

st.title("📄 AI-Powered Document Chatbot")
st.markdown(
    "Upload a PDF document and ask natural-language questions about its content."
)

if not OPENAI_API_KEY:
    st.error("OPENAI_API_KEY not found. Please add it to your .env file.")
    st.stop()

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:
    st.header("Document Upload")
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        try:
            pdf_reader = PdfReader(uploaded_file)

            raw_text = ""
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    raw_text += text

            if raw_text.strip():
                splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000,
                    chunk_overlap=200
                )
                chunks = splitter.split_text(raw_text)

                embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
                vector_store = FAISS.from_texts(chunks, embedding=embeddings)

                st.session_state.vector_store = vector_store
                st.success("PDF processed successfully.")
            else:
                st.error("Could not extract text from the PDF.")

        except Exception as e:
            st.error(f"Error processing PDF: {e}")

    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.success("Chat history cleared.")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Ask Questions")
    question = st.text_input("Enter your question")

    if question and st.session_state.vector_store is not None:
        try:
            docs = st.session_state.vector_store.similarity_search(question, k=4)
            context = "\n\n".join([doc.page_content for doc in docs])

            prompt = f"""
You are a helpful AI assistant for document question answering.

Instructions:
- Answer only using the provided context.
- If the answer is not available in the context, say:
  "I could not find that in the uploaded document."
- Keep the answer clear and concise.
- Where helpful, summarize in bullet points.

Context:
{context}

Question:
{question}
"""

            llm = ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0
            )

            response = llm.invoke(prompt)
            answer = response.content

            st.session_state.chat_history.append(
                {"question": question, "answer": answer, "sources": docs}
            )

        except Exception as e:
            st.error(f"Error answering question: {e}")

    if st.session_state.chat_history:
        st.subheader("Conversation")
        for idx, item in enumerate(reversed(st.session_state.chat_history), start=1):
            with st.expander(f"Q{idx}: {item['question']}", expanded=(idx == 1)):
                st.markdown(f"**Answer:** {item['answer']}")

with col2:
    st.subheader("Retrieved Context")
    if st.session_state.chat_history:
        latest = st.session_state.chat_history[-1]
        for i, doc in enumerate(latest["sources"], start=1):
            st.markdown(f"**Source Chunk {i}:**")
            st.caption(doc.page_content[:500] + ("..." if len(doc.page_content) > 500 else ""))
    else:
        st.info("Retrieved document chunks will appear here after you ask a question.")