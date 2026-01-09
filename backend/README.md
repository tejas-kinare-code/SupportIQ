# SupportIQ Backend

AI Knowledge Assistant Backend built with FastAPI.

## Setup Instructions

### 1. Create Virtual Environment

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Copy `.env.example` to `.env` and update with your configuration:

```bash
cp .env.example .env
```

### 4. Run the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc

## API Endpoints

### Health Check
- `GET /api/health` - Check API health status

### Chat
- `POST /api/chat` - Send a chat message
- `GET /api/chat/{conversation_id}/history` - Get conversation history
- `DELETE /api/chat/{conversation_id}` - Delete a conversation

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── models/              # Pydantic models
│   │   ├── __init__.py
│   │   └── chat.py
│   └── routes/              # API routes
│       ├── __init__.py
│       ├── health.py
│       └── chat.py
├── requirements.txt
├── .env.example
└── README.md
```

## Development Notes

- Currently using in-memory storage for conversations (will be replaced with database later)
- Chat endpoint returns placeholder responses (LangChain integration pending)
- CORS is configured for React frontend on ports 3000 and 5173


