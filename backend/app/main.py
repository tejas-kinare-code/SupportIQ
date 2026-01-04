from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import chat
from app.config import CORS_ORIGINS, API_PREFIX

app = FastAPI(
    title="SupportIQ API",
    description="AI Knowledge Assistant for Enterprise Support",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router, prefix=API_PREFIX)


@app.get("/")
async def root():
    """Root endpoint for health check."""
    return {
        "message": "SupportIQ API is running",
        "version": "1.0.0",
        "docs": "/docs"
    }

