from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama
from app.langchain.vectore_store import create_or_load_vector_store
from app.langchain.text_splitter import chunk_documents
from app.langchain.document_loader import load_documents_by_department


def get_rag_response(query: str, department: str) -> str:
    documents = load_documents_by_department(department)
    chunks = chunk_documents(documents)
    vector_store = create_or_load_vector_store(chunks, department)
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})
    
    llm = ChatOllama(model="llama3", temperature=0)
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False
    )
    
    result = qa_chain.invoke({"query": query})
    return result["result"]
