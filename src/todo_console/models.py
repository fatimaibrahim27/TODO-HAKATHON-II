"""
Models for the Todo Console App
Using only Python standard library components
"""


class TodoItem:
    """
    Represents a single task with content and completion status
    """

    def __init__(self, id_num, content, completed=False):
        """
        Initialize a TodoItem

        Args:
            id_num (int): Unique identifier for the todo item
            content (str): The actual todo text/content
            completed (bool): Current status - False (incomplete) or True (complete)
        """
        if not isinstance(id_num, int) or id_num <= 0:
            raise ValueError("ID must be a positive integer")

        if not isinstance(content, str) or not content.strip():
            raise ValueError("Content must be a non-empty string")

        if not isinstance(completed, bool):
            raise ValueError("Completed must be a boolean value")

        self.id = id_num
        self.content = content.strip()
        self.completed = completed

    def __repr__(self):
        """
        String representation of the TodoItem
        """
        status = "x" if self.completed else " "
        return f"[{status}] {self.id}. {self.content}"

    def mark_complete(self):
        """
        Mark the todo item as complete
        """
        self.completed = True

    def mark_incomplete(self):
        """
        Mark the todo item as incomplete
        """
        self.completed = False

    def update_content(self, new_content):
        """
        Update the content of the todo item

        Args:
            new_content (str): The new content for the todo
        """
        if not isinstance(new_content, str) or not new_content.strip():
            raise ValueError("Content must be a non-empty string")
        self.content = new_content.strip()