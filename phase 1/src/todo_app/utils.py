from datetime import datetime
from typing import Optional


def validate_date_format(date_string: str) -> bool:
    """
    Validates if the given date string is in YYYY-MM-DD format
    """
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def format_todo_display(todo, index: int) -> str:
    """
    Formats a todo item for display in the list
    """
    status_symbol = "✓" if todo.status == "done" else "○"
    priority_symbol = {"low": "L", "medium": "M", "high": "H"}[todo.priority]

    # Format due date if present
    due_str = f" (due: {todo.due_date})" if todo.due_date else ""

    return f"{index}. [{status_symbol}] [{priority_symbol}] {todo.content}{due_str}"


def convert_index_to_zero_based(user_index: int) -> int:
    """
    Converts 1-based user index to 0-based internal index
    """
    return user_index - 1


def validate_priority(priority: str) -> bool:
    """
    Validates if the given priority is one of the allowed values
    """
    return priority in ['low', 'medium', 'high']


def format_error_message(error: Exception) -> str:
    """
    Formats an error message for user display
    """
    return f"Error: {str(error)}"