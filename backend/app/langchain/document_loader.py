from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from typing import List
from langchain_core.documents import Document
from app.config import DATA_DIR


def load_documents_by_department(department: str) -> List[Document]:
    department = department.lower()
    path = DATA_DIR / department
    
    if not path.exists():
        raise ValueError(f"Department folder not found: {department}")
    
    loader = DirectoryLoader(
        path=str(path),
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )

    documents = loader.load()
    return documents

