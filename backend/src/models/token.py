from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class TokenBase(SQLModel):
    token: str = Field(unique=True, nullable=False, max_length=500)
    user_id: uuid.UUID = Field(foreign_key="user.id")
    expires_at: datetime = Field(nullable=False)
    is_revoked: bool = Field(default=False)

class Token(TokenBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class TokenRead(TokenBase):
    id: uuid.UUID
    created_at: datetime

class TokenCreate(TokenBase):
    pass