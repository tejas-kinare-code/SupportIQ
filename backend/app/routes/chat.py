from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.langchain.rag_service import get_rag_response
from app.langchain.intent_classifier import detect_department
from app.langchain.llm_service import get_direct_llm_response


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        department = detect_department(request.message)
        print("department is ", department)
        
        # Use direct LLM for general queries (greetings, casual conversation)
        # Use RAG for hr/it queries (need knowledge base)
        if department == "general":
            response = get_direct_llm_response(request.message)
            print("Direct LLM response:", response)
        else:
            response = get_rag_response(request.message, department)
            print("RAG response:", response)
        
        return ChatResponse(response=response)
    
    except ValueError as e:
        error_detail = f"ValueError: {str(e)}"
        print(error_detail)
        raise HTTPException(status_code=400, detail=error_detail)
    except Exception as e:
        import traceback
        error_detail = f"Error: {str(e)}\n{traceback.format_exc()}"
        print(error_detail)
        raise HTTPException(status_code=500, detail=str(e))

