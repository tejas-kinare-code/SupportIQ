from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama
from app.langchain.vectore_store import create_or_load_vector_store
from app.langchain.text_splitter import chunk_documents
from app.langchain.document_loader import load_documents_by_department
from app.config import MAX_DISTANCE_THRESHOLD


def _has_low_relevance(response_text: str) -> bool:
    """Check if response indicates no relevant information found."""
    negative_indicators = [
        "i don't see",
        "i don't have",
        "not aware",
        "no information",
        "doesn't mention",
        "unable to find",
        "cannot find",
        "not available",
        "not provided"
    ]
    response_lower = response_text.lower()
    return any(indicator in response_lower for indicator in negative_indicators)


def get_rag_response(query: str, department: str) -> str:
    """Get RAG response using knowledge base. Department should be 'hr' or 'it'."""
    documents = load_documents_by_department(department)
    chunks = chunk_documents(documents)
    vector_store = create_or_load_vector_store(chunks, department)
    
    # Check similarity scores before generating response
    similar_docs_with_scores = vector_store.similarity_search_with_score(query, k=4)
    
    if similar_docs_with_scores:
        # Get the minimum distance (best match)
        # FAISS returns L2 distance - lower distance = higher similarity
        min_distance = min(score for _, score in similar_docs_with_scores)
        
        if min_distance > MAX_DISTANCE_THRESHOLD:
            return "I couldn't find relevant information in the knowledge base for your query. Please raise a ticket through the support system for further assistance."
    
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})
    llm = ChatOllama(model="llama3", temperature=0)
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False
    )
    
    result = qa_chain.invoke({"query": query})
    response = result["result"]
    
    # Check if response indicates no relevant information
    if _has_low_relevance(response):
        response += "\n\nIf this information is not available in the knowledge base, please raise a ticket through the support system for further assistance."
    
    return response
