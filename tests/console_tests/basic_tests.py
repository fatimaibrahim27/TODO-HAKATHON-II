"""
Basic tests for the Todo Console App components
Using only Python standard library for testing
"""
import sys
import os

# Add the src directory to the path to import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from todo_console.models import TodoItem
from todo_console.storage import TodoList
from todo_console.commands import CommandProcessor


def test_todo_item():
    """Test TodoItem model"""
    print("Testing TodoItem model...")

    # Test basic creation
    item = TodoItem(1, "Test todo")
    assert item.id == 1
    assert item.content == "Test todo"
    assert item.completed == False

    # Test mark complete/incomplete
    item.mark_complete()
    assert item.completed == True

    item.mark_incomplete()
    assert item.completed == False

    # Test update content
    item.update_content("Updated content")
    assert item.content == "Updated content"

    # Test error cases
    try:
        TodoItem(-1, "Invalid ID")
        assert False, "Should have raised ValueError for negative ID"
    except ValueError:
        pass

    try:
        TodoItem(1, "")
        assert False, "Should have raised ValueError for empty content"
    except ValueError:
        pass

    print("✓ TodoItem tests passed")


def test_todo_list():
    """Test TodoList storage"""
    print("Testing TodoList storage...")

    todo_list = TodoList()

    # Test adding todos
    id1 = todo_list.add("First todo")
    id2 = todo_list.add("Second todo")
    assert id1 == 1
    assert id2 == 2

    # Test getting todos
    item = todo_list.get(1)
    assert item is not None
    assert item.content == "First todo"

    # Test updating todos
    result = todo_list.update(1, "Updated first todo")
    assert result == True
    item = todo_list.get(1)
    assert item.content == "Updated first todo"

    # Test marking complete/incomplete
    result = todo_list.mark_complete(1)
    assert result == True
    item = todo_list.get(1)
    assert item.completed == True

    result = todo_list.mark_incomplete(1)
    assert result == True
    item = todo_list.get(1)
    assert item.completed == False

    # Test listing todos
    all_todos = todo_list.list_all()
    assert len(all_todos) == 2

    completed_todos = todo_list.list_completed()
    assert len(completed_todos) == 0

    # Mark second as complete and test again
    todo_list.mark_complete(2)
    completed_todos = todo_list.list_completed()
    assert len(completed_todos) == 1

    incomplete_todos = todo_list.list_incomplete()
    assert len(incomplete_todos) == 1

    # Test deleting todos
    result = todo_list.delete(1)
    assert result == True
    item = todo_list.get(1)
    assert item is None

    # Verify IDs were updated properly after deletion
    remaining_items = todo_list.list_all()
    assert len(remaining_items) == 1
    assert remaining_items[0].id == 1  # ID should have been updated to maintain sequence

    print("✓ TodoList tests passed")


def test_command_processor():
    """Test CommandProcessor"""
    print("Testing CommandProcessor...")

    processor = CommandProcessor()

    # Test add command
    success, response = processor.process_command("add Buy groceries")
    assert success == True
    assert "Added todo #1" in response

    # Test view command
    success, response = processor.process_command("view")
    assert success == True
    assert "Buy groceries" in response

    # Test update command
    success, response = processor.process_command("update 1 Buy weekly groceries")
    assert success == True
    assert "Updated todo #1" in response

    # Test complete command
    success, response = processor.process_command("complete 1")
    assert success == True
    assert "Marked todo #1 as complete" in response

    # Test delete command
    success, response = processor.process_command("add Another task")
    assert success == True
    success, response = processor.process_command("delete 2")
    assert success == True
    assert "Deleted todo #2" in response

    # Test help command
    success, response = processor.process_command("help")
    assert success == True
    assert "Available commands:" in response

    # Test unknown command
    success, response = processor.process_command("unknowncommand")
    assert success == False
    assert "Unknown command" in response

    print("✓ CommandProcessor tests passed")


def run_all_tests():
    """Run all tests"""
    print("Running Todo Console App tests...\n")

    test_todo_item()
    test_todo_list()
    test_command_processor()

    print("\n✓ All tests passed!")


if __name__ == "__main__":
    run_all_tests()