import streamlit as st
from chains.qa_retriever import create_rag_chain
from loaders.document_loader import load_documents
from config.config import PDF_PATH
from utils.text_splitter import split_documents
from utils.vectorestore import create_vectorstore


def financial_report():
    st.set_page_config(page_title="Financial RAG Insights", layout="centered")
    st.title("\U0001f4b0 Financial Statement Analyzer (RAG POC)")
    query = st.text_input("Enter your financial insight query")

    if query:
        with st.spinner("Analyzing file and generating insights..."):
            documents = load_documents(pdf_path=PDF_PATH)
            chunks = split_documents(documents)
            vectorestore = create_vectorstore(chunks)
            rag_chain = create_rag_chain(vectorestore)
            result = rag_chain.invoke({"input": query})
            st.subheader("\U0001f4c8 Insight Result")
            st.write(result["answer"])
    else:
        st.info("Please enter a query to get started.")
