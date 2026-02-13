from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import create_db_and_tables
from .routers import auth, todos
import os

# Create FastAPI app
app = FastAPI(
    title="Todo API",
    description="Secure Todo API with authentication and CRUD operations",
    version="1.0.0"
)

# Configure CORS for production and development
allowed_origins = [
    "http://localhost:3000",  # Local development
    "http://localhost:8000",  # Local backend
]

# Add production frontend URL from environment variable
frontend_url = os.getenv("FRONTEND_URL")
if frontend_url:
    allowed_origins.append(frontend_url)
    # Also allow Vercel preview deployments
    allowed_origins.append("https://*.vercel.app")

# Add CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins if frontend_url else ["*"],  # Allow all in dev, specific in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with /api prefix
app.include_router(auth.router, prefix="/api")
app.include_router(todos.router, prefix="/api")

@app.on_event("startup")
def on_startup():
    """Initialize database tables on startup."""
    create_db_and_tables()

@app.get("/")
def read_root():
    """Root endpoint for health check."""
    return {"message": "Todo API is running"}

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "Todo API"}