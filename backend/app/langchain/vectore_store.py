from langchain_community.vectorstores import FAISS
from app.config import VECTOR_DB_DIR


def create_or_load_vector_store(chunks, department: str):
    department = department.lower()
    dept_path = VECTOR_DB_DIR / department
    
    VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)
    dept_path.mkdir(parents=True, exist_ok=True)

    from langchain_ollama import OllamaEmbeddings
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    if (dept_path / "index.faiss").exists():
        return FAISS.load_local(
            str(dept_path),
            embeddings,
            allow_dangerous_deserialization=True
        )

    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(str(dept_path))
    return vector_store
