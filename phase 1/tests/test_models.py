import pytest
from src.todo_app.models import TodoItem
from datetime import date, datetime


def test_todo_item_creation():
    """Test creating a basic TodoItem"""
    todo = TodoItem(id=1, content="Test todo")

    assert todo.id == 1
    assert todo.content == "Test todo"
    assert todo.status == "pending"
    assert todo.priority == "medium"
    assert todo.due_date is None
    assert isinstance(todo.created_at, datetime)


def test_todo_item_with_properties():
    """Test creating a TodoItem with all properties"""
    due_date = date(2026, 12, 31)
    created_time = datetime.now()

    todo = TodoItem(
        id=1,
        content="Important task",
        status="done",
        priority="high",
        due_date=due_date,
        created_at=created_time
    )

    assert todo.id == 1
    assert todo.content == "Important task"
    assert todo.status == "done"
    assert todo.priority == "high"
    assert todo.due_date == due_date
    assert todo.created_at == created_time


def test_todo_item_defaults():
    """Test that TodoItem sets correct defaults"""
    todo = TodoItem(id=1, content="Test todo")

    assert todo.status == "pending"
    assert todo.priority == "medium"
    assert todo.due_date is None
    assert isinstance(todo.created_at, datetime)


def test_todo_item_status_validation():
    """Test that TodoItem validates status"""
    # Valid statuses should work
    TodoItem(id=1, content="Test", status="pending")
    TodoItem(id=1, content="Test", status="done")

    # Invalid status should raise ValueError
    with pytest.raises(ValueError, match="Status must be 'pending' or 'done'"):
        TodoItem(id=1, content="Test", status="invalid")


def test_todo_item_priority_validation():
    """Test that TodoItem validates priority"""
    # Valid priorities should work
    TodoItem(id=1, content="Test", priority="low")
    TodoItem(id=1, content="Test", priority="medium")
    TodoItem(id=1, content="Test", priority="high")

    # Invalid priority should raise ValueError
    with pytest.raises(ValueError, match="Priority must be 'low', 'medium', or 'high'"):
        TodoItem(id=1, content="Test", priority="invalid")


def test_todo_item_content_validation():
    """Test that TodoItem validates content"""
    # Valid content should work
    TodoItem(id=1, content="Valid content")

    # Empty content should raise ValueError
    with pytest.raises(ValueError, match="Content cannot be empty or whitespace only"):
        TodoItem(id=1, content="")

    # Whitespace-only content should raise ValueError
    with pytest.raises(ValueError, match="Content cannot be empty or whitespace only"):
        TodoItem(id=1, content="   ")

    with pytest.raises(ValueError, match="Content cannot be empty or whitespace only"):
        TodoItem(id=1, content="\t\n")


def test_todo_item_auto_timestamp():
    """Test that TodoItem automatically sets created_at"""
    todo = TodoItem(id=1, content="Test todo")

    assert isinstance(todo.created_at, datetime)

    # The timestamp should be close to the current time
    time_diff = abs((datetime.now() - todo.created_at).total_seconds())
    assert time_diff < 1  # Should be created within 1 second of now