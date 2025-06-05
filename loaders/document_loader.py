from langchain_community.document_loaders import PyPDFLoader


def load_documents(pdf_path: str):
    pdf_docs = PyPDFLoader(pdf_path).load()
    return pdf_docs
