"""Chat API routes."""
from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.langchain.chat_service import process_message
from app.langchain.text_splitter import chunk_documents
from app.langchain.document_loader import load_documents_by_department


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Load documents for testing (will be replaced with intent-based routing)
        documents = load_documents_by_department("it")
        chunks = chunk_documents(documents)
        print(f"Loaded {len(chunks)} document chunks")
        
        # Process the message
        response = process_message(request.message)
        return ChatResponse(response=response)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat request: {str(e)}")

