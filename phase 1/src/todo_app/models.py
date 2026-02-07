from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional


@dataclass
class TodoItem:
    """
    Represents a single task with content, status, priority, and optional due date
    """
    id: int
    content: str
    status: str = "pending"  # "pending" or "done"
    priority: str = "medium"  # "low", "medium", or "high"
    due_date: Optional[date] = None
    created_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

        # Validate status
        if self.status not in ["pending", "done"]:
            raise ValueError(f"Status must be 'pending' or 'done', got '{self.status}'")

        # Validate priority
        if self.priority not in ["low", "medium", "high"]:
            raise ValueError(f"Priority must be 'low', 'medium', or 'high', got '{self.priority}'")

        # Validate content is not empty
        if not self.content.strip():
            raise ValueError("Content cannot be empty or whitespace only")