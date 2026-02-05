import pytest
from src.todo_app.storage import TodoStorage
from src.todo_app.models import TodoItem
from datetime import date


@pytest.fixture
def storage():
    return TodoStorage()


def test_storage_add_and_list(storage):
    """Test adding and retrieving todos from storage"""
    # Create a todo item
    todo = TodoItem(id=0, content="Test todo")

    # Add to storage
    todo_id = storage.add(todo)

    # Verify the ID was assigned correctly
    assert todo_id == 1
    assert storage.next_id == 2

    # Verify the todo is in the list
    todos = storage.list_all()
    assert len(todos) == 1
    assert todos[0].id == 1
    assert todos[0].content == "Test todo"


def test_storage_get_by_index(storage):
    """Test getting a todo by index"""
    # Add a couple of todos
    todo1 = TodoItem(id=0, content="First todo")
    todo2 = TodoItem(id=0, content="Second todo")

    storage.add(todo1)
    storage.add(todo2)

    # Test getting first todo (index 0)
    retrieved = storage.get(0)
    assert retrieved is not None
    assert retrieved.content == "First todo"

    # Test getting second todo (index 1)
    retrieved = storage.get(1)
    assert retrieved is not None
    assert retrieved.content == "Second todo"

    # Test getting non-existent todo
    retrieved = storage.get(10)
    assert retrieved is None


def test_storage_update(storage):
    """Test updating a todo's properties"""
    # Add a todo
    todo = TodoItem(id=0, content="Original todo")
    storage.add(todo)

    # Update the content
    success = storage.update(0, content="Updated todo")
    assert success is True

    # Verify the update
    updated_todo = storage.get(0)
    assert updated_todo.content == "Updated todo"

    # Test updating other properties
    success = storage.update(0, priority="high", status="done")
    assert success is True

    updated_todo = storage.get(0)
    assert updated_todo.priority == "high"
    assert updated_todo.status == "done"

    # Test updating non-existent todo
    success = storage.update(10, content="Invalid update")
    assert success is False


def test_storage_delete(storage):
    """Test deleting a todo"""
    # Add a couple of todos
    todo1 = TodoItem(id=0, content="First todo")
    todo2 = TodoItem(id=0, content="Second todo")

    storage.add(todo1)
    storage.add(todo2)

    # Verify both exist
    todos = storage.list_all()
    assert len(todos) == 2

    # Delete the first one
    success = storage.delete(0)
    assert success is True

    # Verify deletion
    todos = storage.list_all()
    assert len(todos) == 1
    assert todos[0].content == "Second todo"
    assert todos[0].id == 1  # ID should be adjusted

    # Try to delete non-existent todo
    success = storage.delete(10)
    assert success is False


def test_storage_mark_done_pending(storage):
    """Test marking todos as done and pending"""
    # Add a todo
    todo = TodoItem(id=0, content="Test todo")
    storage.add(todo)

    # Mark as done
    success = storage.mark_done(0)
    assert success is True

    # Verify status
    todo = storage.get(0)
    assert todo.status == "done"

    # Mark as pending
    success = storage.mark_pending(0)
    assert success is True

    # Verify status
    todo = storage.get(0)
    assert todo.status == "pending"

    # Test with non-existent todo
    success = storage.mark_done(10)
    assert success is False


def test_storage_empty_list(storage):
    """Test behavior with empty storage"""
    # Initially should be empty
    todos = storage.list_all()
    assert len(todos) == 0

    # Try to get from empty storage
    todo = storage.get(0)
    assert todo is None

    # Try to update/delete from empty storage
    assert storage.update(0, content="test") is False
    assert storage.delete(0) is False
    assert storage.mark_done(0) is False
    assert storage.mark_pending(0) is False


def test_storage_with_due_date_and_priority(storage):
    """Test storage with various todo properties"""
    # Create todo with due date and priority
    due_date = date(2026, 12, 31)
    todo = TodoItem(
        id=0,
        content="Important task",
        priority="high",
        due_date=due_date
    )

    # Add to storage
    storage.add(todo)

    # Retrieve and verify properties
    retrieved = storage.get(0)
    assert retrieved.content == "Important task"
    assert retrieved.priority == "high"
    assert retrieved.due_date == due_date
    assert retrieved.status == "pending"