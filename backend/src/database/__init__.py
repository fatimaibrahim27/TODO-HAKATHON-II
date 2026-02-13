from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlmodel import Session, SQLModel
from typing import Generator
import os
from contextlib import contextmanager

# Import all models to ensure they're registered with SQLModel
from ..models.user import User
from ..models.todo import Todo

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo.db")

print(f"[Database] Connecting to: {DATABASE_URL[:30]}...")  # Log connection (truncated for security)

# Create engine with connection pooling
# For SQLite, we use simpler configuration
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}  # Needed for SQLite
    )
else:
    engine = create_engine(
        DATABASE_URL,
        poolclass=QueuePool,
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True,  # Verify connections before use
        pool_recycle=300,    # Recycle connections after 5 minutes
    )

def create_db_and_tables():
    """Create database tables if they don't exist"""
    try:
        print("[Database] Creating tables...")
        SQLModel.metadata.create_all(engine)
        print("[Database] Tables created successfully!")
    except Exception as e:
        print(f"[Database] Error creating tables: {e}")
        raise

def get_session() -> Generator[Session, None, None]:
    """Dependency for FastAPI to provide database session."""
    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()