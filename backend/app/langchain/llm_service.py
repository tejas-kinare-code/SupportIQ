from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate


def get_direct_llm_response(query: str) -> str:
    """Get direct LLM response without RAG for general queries, greetings, etc."""
    llm = ChatOllama(model="llama3", temperature=0.7)
    
    prompt = ChatPromptTemplate.from_template(
        """
        You are a helpful AI assistant for an enterprise internal support system.
        Respond to the user's query in a friendly and professional manner.
        
        If it's a greeting, respond warmly and offer to help with HR or IT questions.
        If it's a general question, answer helpfully but suggest raising a ticket if it requires specific company information not available to you.
        
        Keep responses concise and professional.
        
        User query: {query}
        Response:
        """
    )
    
    response = llm.invoke(prompt.format_messages(query=query))
    return response.content.strip()

