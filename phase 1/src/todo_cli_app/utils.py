"""
Utilities layer for the Todo CLI App
Provides validation, formatting, and helper functions
"""


class TodoTask:
    """
    Represents a single task with ID, content, and completion status
    """

    def __init__(self, task_id, content, completed=False):
        """
        Initialize a TodoTask

        Args:
            task_id (int): Unique identifier for the task
            content (str): The task description/content
            completed (bool): Status indicator - False (incomplete) or True (complete)
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if not isinstance(content, str) or not content.strip():
            raise ValueError("Task content must be a non-empty string")

        if not isinstance(completed, bool):
            raise ValueError("Completed must be a boolean value")

        self.id = task_id
        self.content = content.strip()
        self.completed = completed

    def __repr__(self):
        """
        String representation of the task
        """
        status = "x" if self.completed else " "
        return f"[{status}] {self.id}. {self.content}"

    def mark_complete(self):
        """
        Mark the task as complete
        """
        self.completed = True

    def mark_incomplete(self):
        """
        Mark the task as incomplete
        """
        self.completed = False

    def update_content(self, new_content):
        """
        Update the content of the task

        Args:
            new_content (str): The new content for the task
        """
        if not isinstance(new_content, str) or not new_content.strip():
            raise ValueError("Task content must be a non-empty string")
        self.content = new_content.strip()


def validate_task_content(content):
    """
    Validate task content

    Args:
        content (str): Content to validate

    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(content, str):
        return False
    return bool(content.strip())


def validate_task_id(task_id):
    """
    Validate task ID

    Args:
        task_id (int): ID to validate

    Returns:
        bool: True if valid, False otherwise
    """
    return isinstance(task_id, int) and task_id > 0


def format_task_list(tasks):
    """
    Format a list of tasks for display

    Args:
        tasks (list): List of TodoTask objects

    Returns:
        str: Formatted string representation of tasks
    """
    if not tasks:
        return "No tasks found."

    lines = ["Tasks:"]
    for task in tasks:
        lines.append(str(task))
    return "\n".join(lines)


def parse_command(command_line):
    """
    Parse a command line into command and arguments

    Args:
        command_line (str): Raw command line from user

    Returns:
        tuple: (command, args) parsed command and arguments
    """
    if not command_line or not command_line.strip():
        return "", []

    parts = command_line.strip().split()
    command = parts[0].lower()
    args = parts[1:]

    return command, args