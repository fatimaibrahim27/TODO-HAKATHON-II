import pytest
from src.todo_app.cli import cli
from src.todo_app.storage import TodoStorage
from src.todo_app.models import TodoItem
from datetime import date
from click.testing import CliRunner


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def storage():
    return TodoStorage()


def test_add_and_list_todos(runner, storage):
    """Test adding and listing todos functionality"""
    # Mock global storage in cli module temporarily for testing
    import src.todo_app.cli as cli_module
    original_storage = cli_module.storage
    cli_module.storage = storage

    try:
        # Test adding a todo
        result = runner.invoke(cli, ['add', 'Buy groceries'])
        assert result.exit_code == 0
        assert 'Added todo #1: Buy groceries' in result.output

        # Test listing todos
        result = runner.invoke(cli, ['list'])
        assert result.exit_code == 0
        assert 'Buy groceries' in result.output
        assert '[○]' in result.output  # Pending status
        assert '[M]' in result.output  # Medium priority
    finally:
        # Restore original storage
        cli_module.storage = original_storage


def test_update_todo(runner, storage):
    """Test updating a todo functionality"""
    import src.todo_app.cli as cli_module
    original_storage = cli_module.storage
    cli_module.storage = storage

    try:
        # Add a todo first
        result = runner.invoke(cli, ['add', 'Buy groceries'])
        assert result.exit_code == 0

        # Update the todo
        result = runner.invoke(cli, ['update', '1', 'Buy weekly groceries'])
        assert result.exit_code == 0
        assert 'Updated todo #1' in result.output

        # Verify the update by listing
        result = runner.invoke(cli, ['list'])
        assert 'Buy weekly groceries' in result.output
    finally:
        cli_module.storage = original_storage


def test_delete_todo(runner, storage):
    """Test deleting a todo functionality"""
    import src.todo_app.cli as cli_module
    original_storage = cli_module.storage
    cli_module.storage = storage

    try:
        # Add a todo first
        result = runner.invoke(cli, ['add', 'Buy groceries'])
        assert result.exit_code == 0

        # Delete the todo
        result = runner.invoke(cli, ['delete', '1'])
        assert result.exit_code == 0
        assert 'Deleted todo #1' in result.output

        # Verify deletion by listing
        result = runner.invoke(cli, ['list'])
        assert 'No todos found.' in result.output
    finally:
        cli_module.storage = original_storage


def test_mark_done_pending(runner, storage):
    """Test marking todos as done/pending functionality"""
    import src.todo_app.cli as cli_module
    original_storage = cli_module.storage
    cli_module.storage = storage

    try:
        # Add a todo first
        result = runner.invoke(cli, ['add', 'Buy groceries'])
        assert result.exit_code == 0

        # Mark as done
        result = runner.invoke(cli, ['done', '1'])
        assert result.exit_code == 0
        assert 'Marked todo #1 as done' in result.output

        # Verify done status by listing
        result = runner.invoke(cli, ['list'])
        assert '[✓]' in result.output  # Done status

        # Mark as pending
        result = runner.invoke(cli, ['pending', '1'])
        assert result.exit_code == 0
        assert 'Marked todo #1 as pending' in result.output

        # Verify pending status by listing
        result = runner.invoke(cli, ['list'])
        assert '[○]' in result.output  # Pending status
    finally:
        cli_module.storage = original_storage


def test_add_todo_with_priority_and_due_date(runner, storage):
    """Test adding a todo with priority and due date"""
    import src.todo_app.cli as cli_module
    original_storage = cli_module.storage
    cli_module.storage = storage

    try:
        # Add a todo with priority and due date
        result = runner.invoke(cli, [
            'add', 'Finish report',
            '--priority', 'high',
            '--due', '2026-12-31'
        ])
        assert result.exit_code == 0
        assert 'Added todo #1: Finish report' in result.output

        # Verify by listing
        result = runner.invoke(cli, ['list'])
        assert 'Finish report' in result.output
        assert '[H]' in result.output  # High priority
        assert 'due: 2026-12-31' in result.output
    finally:
        cli_module.storage = original_storage