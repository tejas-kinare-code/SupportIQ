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
        Classify the user query into ONE department: hr, it, or general.

        Examples:
        Query: "How many leaves can I take in a year?" → hr
        Query: "What is my notice period?" → hr
        Query: "I need help with VPN connection" → it
        Query: "My laptop is not working" → it
        Query: "What is the company address?" → general
        Query: "Tell me about the cafeteria" → general

        Return ONLY one lowercase word: hr, it, or general

        User query: {query}
        Department:
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
