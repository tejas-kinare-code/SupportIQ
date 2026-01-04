from fastapi import APIRouter
from pydantic import BaseModel
from app.langchain.service import firstReceivedMessage

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat(request: ChatRequest):
    response = firstReceivedMessage(request.message)
    return {"response": response}

