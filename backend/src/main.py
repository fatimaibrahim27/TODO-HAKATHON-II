from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import create_db_and_tables
from .routers import auth, todos

# Create FastAPI app
app = FastAPI(
    title="Todo API",
    description="Secure Todo API with authentication and CRUD operations",
    version="1.0.0"
)

# Add CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(todos.router)

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