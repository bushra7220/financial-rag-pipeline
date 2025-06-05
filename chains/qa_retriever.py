from langchain_openai import ChatOpenAI
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from utils.template_prompt import get_financial_prompt


def create_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    llm = ChatOpenAI(verbose=True, temperature=0)
    prompt = get_financial_prompt()
    document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)

    return create_retrieval_chain(
        retriever=retriever, combine_docs_chain=document_chain
    )