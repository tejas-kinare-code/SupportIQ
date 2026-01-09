from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate


def detect_department(query: str) -> str:
    """
    Classifies user query into one of:
    hr, it, finance, general
    """

    llm = ChatOllama(
        model="llama3",
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template(
        """
        You are an intent classifier for an enterprise internal support system.
        Classify the user query into ONE category: hr, it, or general.

        Use RAG (hr/it) when the query needs information from company policies, procedures, or documentation.
        Use general (direct LLM) for greetings, casual conversation, or queries not related to company policies.

        Examples:
        Query: "How many leaves can I take in a year?" → hr (needs leave policy document)
        Query: "What is my notice period?" → hr (needs HR policy document)
        Query: "I need help with VPN connection" → it (needs IT documentation)
        Query: "My laptop is not working" → it (needs IT support documentation)
        Query: "Hi" → general (greeting, no documentation needed)
        Query: "Hello, how are you?" → general (casual conversation)
        Query: "What is the company address?" → general (general question, not in policy docs)
        Query: "Tell me about the cafeteria" → general (not in knowledge base)

        Return ONLY one lowercase word: hr, it, or general

        User query: {query}
        Category:
        """
    )

    response = llm.invoke(
        prompt.format_messages(query=query)
    )

    department = response.content.strip().lower()

    # Safety fallback
    if department not in {"hr", "it", "general"}:
        return "general"

    return department
